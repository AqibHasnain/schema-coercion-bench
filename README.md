# schema-coercion-bench

A small benchmark for automated schema coercion: turning messy, human-made tables into records
that validate against a fixed Pydantic schema.

Each task gives you one or more raw tables (CSV, TSV or XLSX) and a Pydantic model file. The job
is to produce one clean table per target class whose rows validate against that class. Most tasks
include a hand-written reference output to score against.

## The task

A system under test receives:

- `inputs/`: the raw files, exactly as a person might export them from a spreadsheet or LIMS.
- `model`: a Python file of Pydantic v2 models (fields, types, enums, descriptions).
- `target_classes`: the model classes to populate.

It must return, for each target class, a table whose columns are that class's fields and whose
rows are the entities found in the inputs. Doing that well takes several distinct skills, and
the tasks are built to exercise each one:

- **Schema mapping.** Match input columns to model fields when headers are renamed, abbreviated,
  reordered, split across columns or mixed with irrelevant columns (`Mass of the Body` ->
  `Body_Mass__pounds_`, `is_random` -> `randomization`).
- **Type coercion and unit normalization.** Parse numbers carrying units and convert them to the
  unit the field names (`11.34kg` -> pounds, `80000g` -> 80 kg, `32` F -> 0 C, `10yr` -> `10` +
  `Years`).
- **Date and time normalization.** Reconcile `January 1st, 2023`, `1/2/23`, `5th Oct 2024`,
  `"5- 6 -2024"` and `24-12-2023` into one consistent date format.
- **Error correction.** Fix casing, stray whitespace, typos and malformed values (`wEirD CapS`,
  `extra whitespace  `), and leave a value empty when it cannot be recovered.
- **Entity canonicalization.** Map free text onto controlled vocabularies and enums (`human` ->
  `Homo sapiens`, `carcinoma`/`cancer` -> `Carcinoma`, `1/2 Indian 1/4 caucasian 1/4 chinese` ->
  `['asian', 'caucasian']`, `Yes`/`Unknown` -> boolean or null).
- **List and compound values.** Split packed cells (`"[OSKM,LINE1]"` -> `Perturbation_1`,
  `Perturbation_2`; `"Fever, Weakness"` -> `['fever', 'weakness']`).
- **Harmonization across files.** Combine several inputs describing the same entities: row-wise
  tables plus a transposed one (`clinical/e6`), records split across files (`strain/mom3`,
  `experiment/mom7`) and multi-sheet workbooks that need a merge or join (`experiment/mom1_*`).
- **Relational linking.** Populate reference fields between classes (a `Treatment` points to its
  `Tumor`, an `Appointment` to its `Patient`) and deduplicate entities that appear in more than
  one file.
- **Ambiguity.** Some inputs have more than one defensible reading. Those tasks ship every
  accepted answer (`<Class>.possibility1.xlsx`, `<Class>.possibility2.xlsx`).

## Layout

```
models/                     Pydantic schema files
tasks/<family>/<task>/
  task.json                 model, target classes, inputs, expected outputs, notes
  inputs/                   raw files to coerce
  expected/                 reference outputs, one file per target class
MANIFEST.csv                sha256 and size of every data file
```

A `task.json`:

```json
{
  "id": "clinical/e6",
  "model": "../../../models/mom_pydantic_tumor_patient.py",
  "target_classes": ["Patient"],
  "inputs": ["inputs/e6_patient_data.csv", "inputs/e6_patient_data_2.csv"],
  "expected": ["expected/Patient.possibility1.xlsx", "expected/Patient.possibility2.xlsx"],
  "notes": "Second input is transposed. Two reference outputs; either is a correct answer."
}
```

`model` is relative to the task directory. Where a schema was revised, the file carries a `.vN`
suffix, and each task points at the version its reference output was written against.

## Families

| family | tasks | with reference | what it covers |
|---|---|---|---|
| `benchmark` | 16 | 15 | Generated tables named `test_<Class>_<N>attr_<M>cols_20rows`: M messy columns that map onto N fields of one class. Varying M at fixed N measures robustness to distractor and split columns. |
| `synthetic` | 4 | 3 | Synthetic-organism and Organism records with messy units, casing, dates and packed lists. |
| `experiment` | 12 | 4 | Bacterial growth experiments, including multi-sheet workbooks that need a merge or join. |
| `strain` | 1 | 1 | Bacterial strain records split across two files. |
| `clinical` | 10 | 10 | Patient, Tumor, Treatment and Appointment records: multi-class extraction, cross-file joins, foreign keys, transposed tables and ambiguous values. |
| `moma_atlas` | 1 | 0 | 23 mouse-cohort lab sheets (injury, plasma collection, organ lists) exported from a spreadsheet: merged headers, notes in data cells, one entity spread across many sheets. No target classes are fixed; `pydantic_english.py` defines Organism, Tissue, Organ, ProteomicsSample and request models. |

Tasks without a reference output are still useful for checking that the output validates
against the model.

## Scoring

Score each target class field by field after aligning rows on the class's identifier (or on row
order where there is none). For tasks with several possibilities, take the best match. Apply the
same normalization to both sides before comparing: trim strings, compare numbers with a small
tolerance, parse dates.

The reference outputs are kept as they were written and have some quirks:

- Several CSVs start with an unnamed index column. Ignore it.
- `benchmark/synthetic_*` use the field aliases `Food_mass__kg_` and `Lint_me`.
- `benchmark/vehicle_*` spell the field `transmmission`.
- `benchmark/reagent_5attr_{11,16}cols` have an extra `mithrl_report` column.
- `clinical/{e2,mom4,mom5}` express foreign keys as `refAttr_*` and `*_mithrlRecord` columns
  rather than the model's reference field.
- `benchmark/tumor_30attr_19cols_5attr_subset` uses a 6-field model against the full Tumor
  reference. Score only the model's fields.

All data is toy data. Names and emails are fabricated.
