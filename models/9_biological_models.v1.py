from __future__ import annotations

import re
import sys
from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from typing import Any, Dict, List, Literal, Optional, Union

from pydantic.version import VERSION as PYDANTIC_VERSION

if int(PYDANTIC_VERSION[0]) >= 2:
    from pydantic import AliasChoices, BaseModel, ConfigDict, Field, field_validator
else:
    from pydantic import BaseModel, Field, validator


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra="forbid",
        arbitrary_types_allowed=True,
        use_enum_values=True,
        strict=False,
    )
    pass


class AgeUnitEnum(str, Enum):
    """
    imported from benchling - no description?
    """

    Days = "Days"
    Weeks = "Weeks"
    Months = "Months"
    Years = "Years"
    Others = "Others"


class SpeciesEnum(str, Enum):
    """
    imported from benchling - no description?
    """

    Apis_mellifera = "Apis mellifera"
    Arabidopsis_thaliana = "Arabidopsis thaliana"
    Bos_torus = "Bos torus"
    Branchiostoma_lanceolatum = "Branchiostoma lanceolatum"
    Caenorhabditis_elegans = "Caenorhabditis elegans"
    Callithrix_jacchus = "Callithrix jacchus"
    Canis_familiaris = "Canis familiaris"
    Cavia_porcellus = "Cavia porcellus"
    cricetulus_griseus = "cricetulus griseus"
    Danio_rerio = "Danio rerio"
    Dictyostelium_discoideum = "Dictyostelium discoideum"
    Drosophila_melanogaster = "Drosophila melanogaster"
    Equus_caballus = "Equus caballus"
    Escherichia_coli = "Escherichia coli"
    Felis_catus = "Felis catus"
    Gallus_gallus = "Gallus gallus"
    Homo_sapiens = "Homo sapiens"
    Hydra = "Hydra"
    Macaca_mulatta = "Macaca mulatta"
    Monodelphis_domestica = "Monodelphis domestica"
    Mus_caroli = "Mus caroli"
    Mus_musculus = "Mus musculus"
    Mus_musculus_castaneus = "Mus musculus castaneus"
    non_human_primate = "non-human primate"
    Oryctolagus_cuniculus = "Oryctolagus cuniculus"
    Other = "Other"
    Phi_X_174 = "Phi X 174"
    Rattus_norvegicus = "Rattus norvegicus"
    Saccharomyces_cerevisiae = "Saccharomyces cerevisiae"
    spodoptera_frugiperda = "spodoptera frugiperda"
    spodoptera_frugipersa = "spodoptera frugipersa"
    Sus_scrofa = "Sus scrofa"
    Tetraodon_nigroviridis = "Tetraodon nigroviridis"
    Unknown = "Unknown"
    Xenopus_laevis = "Xenopus laevis"
    Testudo_hermanni = "Testudo hermanni"
    Testudo_graeca = "Testudo graeca"
    Centrochelys_sulcata = "Centrochelys sulcata"
    Chelonoidis_carbonaria = "Chelonoidis carbonaria"
    Terrapene_triunguis = "Terrapene triunguis"
    Varanus_salvadorii = "Varanus salvadorii"
    Varanus_ornatus = "Varanus ornatus"
    Varanus_salvator = "Varanus salvator"
    Pituophis_catenifer_sayi = "Pituophis catenifer sayi"
    Malayopython_reticulatus = "Malayopython reticulatus"
    Cyclura_cornuta = "Cyclura cornuta"
    Rhacodactylus_leachianus = "Rhacodactylus leachianus"
    Chinchilla_lanigera = "Chinchilla lanigera"
    Didelphis_marsupialis = "Didelphis marsupialis"
    Didelphidae = "Didelphidae"
    Chelonoidis_carbonarius = "Chelonoidis carbonarius"
    Peromyscus_maniculatus = "Peromyscus maniculatus"
    # manual add
    Sus_domesticus = "Sus domesticus"


####eveerything after this was added manually for the synthetic dataset
class FailureDetectionEnum(str, Enum):
    """
    imported from benchling - no description?
    """

    foo = "foo"
    bar = "bar"


class DiseaseEnum(str, Enum):
    """
    imported from benchling - no description?
    """

    Actinobacillosis = "Actinobacillosis"
    Aleutian_Mink_Disease = "Aleutian Mink Disease"
    Anal_Gland_Neoplasms = "Anal Gland Neoplasms"
    Anaplasmosis = "Anaplasmosis"
    Bird_Diseases_ = "Bird Diseases"
    Borna_Disease = "Borna Disease"
    Cat_Diseases_ = "Cat Diseases"
    Cattle_Diseases_ = "Cattle Diseases"
    Digital_Dermatitis = "Digital Dermatitis"
    Disease_Models_Animal = "Disease Models Animal"
    Dog_Diseases_ = "Dog Diseases"
    Enterotoxemia = "Enterotoxemia"
    Erysipelothrix_Infections_ = "Erysipelothrix Infections"
    Fish_Diseases_ = "Fish Diseases"
    Foot_and_Mouth_Disease = "Foot-and-Mouth Disease"
    Foot_Rot = "Foot Rot"
    Goat_Diseases = "Goat Diseases"
    Heartwater_Disease = "Heartwater Disease"
    Hepatitis_Animal_ = "Hepatitis Animal"
    Horse_Diseases_ = "Horse Diseases"
    Keratoconjunctivitis_Infectious = "Keratoconjunctivitis Infectious"
    Lameness_Animal = "Lameness Animal"
    Mammary_Neoplasms_Animal = "Mammary Neoplasms Animal"
    Mink_Viral_Enteritis = "Mink Viral Enteritis"
    Muscular_Dystrophy_Animal_ = "Muscular Dystrophy Animal"
    Myxomatosis_Infectious = "Myxomatosis Infectious"
    Parasitic_Diseases_Animal_ = "Parasitic Diseases Animal"
    Paratuberculosis = "Paratuberculosis"
    Parturient_Paresis = "Parturient Paresis"
    Peste_des_Petits_Ruminants = "Peste-des-Petits-Ruminants"
    Pleuropneumonia_Contagious = "Pleuropneumonia Contagious"
    Primate_Diseases_ = "Primate Diseases"
    Pseudorabies = "Pseudorabies"
    Pythiosis = "Pythiosis"
    Rinderpest = "Rinderpest"
    Rodent_Diseases_ = "Rodent Diseases"
    Salmonella_Infections_Animal = "Salmonella Infections Animal"
    Sheep_Diseases_ = "Sheep Diseases"
    Steatitis = "Steatitis"
    Swine_Diseases_ = "Swine Diseases"
    Venereal_Tumors_Veterinary = "Venereal Tumors Veterinary"
    Vesicular_Stomatitis = "Vesicular Stomatitis"
    Wasting_Disease_Chronic = "Wasting Disease Chronic"
    Zoonoses = "Zoonoses"
    Arrhythmia_Sinus_ = "Arrhythmia Sinus"
    Atrial_Fibrillation = "Atrial Fibrillation"
    Atrial_Flutter = "Atrial Flutter"
    Bradycardia = "Bradycardia"
    Brugada_Syndrome = "Brugada Syndrome"
    Cardiac_Complexes_Premature_ = "Cardiac Complexes Premature"
    Commotio_Cordis = "Commotio Cordis"
    Heart_Block_ = "Heart Block"
    Long_QT_Syndrome_ = "Long QT Syndrome"
    Parasystole = "Parasystole"
    Pre_Excitation_Syndromes_ = "Pre-Excitation Syndromes"
    Tachycardia_ = "Tachycardia"
    Ventricular_Fibrillation = "Ventricular Fibrillation"
    Ventricular_Flutter = "Ventricular Flutter"
    Neoplasms = "Neoplasms"
    Carcinoma = "Carcinoma"
    No_disease = "No disease"


class EthnicityEnum(str, Enum):
    """
    imported from benchling - no description?
    """

    hispanic_or_latino = "hispanic or latino"
    not_hispanic_or_latino = "not hispanic or latino"
    unknown = "unknown"
    blackSOLIDUSafrican_american = "black/african american"
    white = "white"
    filipino = "filipino"
    caucasian = "caucasian"
    JAPANESE = "JAPANESE"
    nSOLIDUSa = "n/a"
    asian = "asian"


# class Randomize/UnrandomizedEnum(str, Enum):
class Randomize_UnrandomizedEnum(str, Enum):
    """
    imported from benchling - no description?
    """

    Randomize = "Randomize"
    Unrandomized = "Unrandomized"


class Synthetic(ConfiguredBaseModel):
    """
    imported from benchling - no description?
    """

    Water_Temp__celsius_: Optional[str] = Field(...)
    Body_Mass__pounds_: Optional[str] = Field(...)
    Age: Optional[str] = Field(...)
    Age_Unit: Optional[AgeUnitEnum] = Field(...)
    Perturbation_1: Optional[str] = Field(...)
    Perturbation_2: Optional[str] = Field(...)
    Food_Mass__kg_: Optional[str] = Field(...)
    Disease: Optional[DiseaseEnum] = Field(...)
    Species: Optional[SpeciesEnum] = Field(...)
    Lint_Me: Optional[str] = Field(...)
    Experiment_Date: Optional[datetime] = Field(...)
    failure_detection_test: Optional[FailureDetectionEnum] = Field(...)
    diet: Optional[str] = Field(...)


class Organism(ConfiguredBaseModel):
    """
    imported from benchling - no description?
    """

    Species: SpeciesEnum = Field(..., description="""imported from benchling - no description?""")
    # Sex: SexEnum = Field(..., description="""imported from benchling - no description?""")
    Strain: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Age: Optional[float] = Field(None, description="""imported from benchling - no description?""")
    # Age_Unit_(Weeks_Months_etc.): Optional[AgeUnitEnum] = Field(None, description="""imported from benchling - no description?""")
    Age_Unit: Optional[AgeUnitEnum] = Field(None, description="""imported from benchling - no description?""")
    Line: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Genotype: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Phenotype: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    # Race: Optional[RaceEnum] = Field(None, description="""imported from benchling - no description?""")
    Ethnicity: Optional[List[EthnicityEnum]] = Field(
        default_factory=list, description="""imported from benchling - no description?"""
    )
    # Birth_Date: Optional[datetime ] = Field(None, description="""imported from benchling - no description?""")
    # Death_Date: Optional[datetime ] = Field(None, description="""imported from benchling - no description?""")
    Birth_Date: Optional[date] = Field(None, description="""imported from benchling - no description?""")
    Death_Date: Optional[date] = Field(None, description="""imported from benchling - no description?""")
    Health_Status: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Comorbidities: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Diet: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    # Randomized_/_Unrandomized: Optional[Randomize/UnrandomizedEnum] = Field(None, description="""imported from benchling - no description?""")
    Randomized___Unrandomized: Optional[Randomize_UnrandomizedEnum] = Field(
        None, description="""imported from benchling - no description?"""
    )
    Masking_ID: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Physical_Tag: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    # Parent_Material_ID(s): Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Parent_Material_ID_s_: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    has_Mother_ID: Optional[Organism] = Field(None, description="""imported from benchling - no description?""")
    has_Father_ID: Optional[Organism] = Field(None, description="""imported from benchling - no description?""")
    Mother_Lineage: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Father_Lineage: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Owner_User: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    System: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    System_id: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    organism_id: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    # Wean_Date: Optional[datetime ] = Field(None, description="""imported from benchling - no description?""")
    # Tail_Tag_Date: Optional[datetime ] = Field(None, description="""imported from benchling - no description?""")
    # Mature_Date: Optional[datetime ] = Field(None, description="""imported from benchling - no description?""")
    Wean_Date: Optional[date] = Field(None, description="""imported from benchling - no description?""")
    Tail_Tag_Date: Optional[date] = Field(None, description="""imported from benchling - no description?""")
    Mature_Date: Optional[date] = Field(None, description="""imported from benchling - no description?""")
    Litter_SID: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Mouseline: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Notes: Optional[str] = Field(None, description="""imported from benchling - no description?""")


class OrganTypeEnum(str, Enum):
    brain = "Brain"
    heart = "Heart"
    lung = "Lung"
    kidney = "Kidney"
    skin = "Skin"
    stomach = "Stomach"
    small_intestine = "Small Intestine"
    large_intestine = "Large Intestine"
    pancreas = "Pancreas"
    eye = "Eye"
    ear = "Ear"
    nose = "Nose"
    tongue = "Tongue"
    other = "Other"


# Organ
class HealthStatusEnum(str, Enum):
    healthy = "Healthy"
    diseased = "Diseased"
    unknown = "Unknown"


# Define the Organ class
class Organ(ConfiguredBaseModel):
    organ_type: OrganTypeEnum = Field(..., description="Type of the organ")
    weight: Optional[float] = Field(None, description="Weight of the organ in grams")
    health_status: HealthStatusEnum = Field(..., description="Health status of the organ")
    organism_id: str = Field(..., description="ID of the parent organism")


# Experiment
class Experiment(ConfiguredBaseModel):
    lead_researcher_id: str = Field(..., description="ID of the lead researcher")
    start_date: Optional[datetime] = Field(..., description="Start date of the experiment")
    end_date: Optional[datetime] = Field(..., description="End date of the experiment")
    treatment_id: str = Field(..., description="ID of the treamtment")
    organism_id: str = Field(..., description="ID of the organism")  # This will eventually need to be a list


# Researcher
class Researcher(ConfiguredBaseModel):
    name: str = Field(..., description="Name of the researcher")
    role: str = Field(..., description="Role of the researcher")
    experiment_ids: Optional[List[str]] = Field(
        default_factory=list, description="The list of experiement_ids performed by the researcher."
    )


# Disease
class DiseaseTypeEnum(str, Enum):
    infectious = "Infectious"
    genetic = "Genetic"
    metabolic = "Metabolic"
    external = "External"
    autoimmune = "Autoimmune"
    deficiency = "Deficiency"
    neurological = "Neurological"


class InfectiousAgentEnum(str, Enum):
    virus = "Virus"
    bacteria = "Bacteria"
    fungi = "Fungi"
    parasite = "Parasite"


class BodySystemAgentEnum(str, Enum):
    cardiovasvular = "Cardiovascular System"
    respiratory = "Respiratory System"
    nervous = "Nervous System"
    digestive = "Digestive System"
    endocrine = "Endocrine System"


class Disease(ConfiguredBaseModel):
    disease_type: DiseaseTypeEnum = Field(..., description="Type of the disease")
    infectious_agent_type: InfectiousAgentEnum = Field(..., description="Agent of infection")
    affected_system: BodySystemAgentEnum = Field(..., description="The system in the body that is affected")
    patient_symptoms: str = Field(..., description="Symptoms described by the patient")


# Trial
class Trial(ConfiguredBaseModel):
    title: str
    phase: int = Field(ge=1, le=4)
    start_date: Optional[datetime] = Field(..., description="Start date of the trial")
    end_date: Optional[datetime] = Field(..., description="End date of the trial")
    blinding: str = Field(choices=["open-label", "single-blind", "double-blind"])
    randomization: bool
    placebo_controlled: bool
    comparator: Optional[str]
    researcher_id: Optional[str] = Field(..., description="The id of the researched administrating the trial")
    notes: Optional[str] = Field(..., description="Additional notes or observations")


# Tumor
class TumorTypeEnum(Enum):
    BENIGN = "benign"
    MALIGNANT = "malignant"
    ADENOMA = "adenoma"
    FIBROMA = "fibroma"
    LIPOMA = "lipoma"
    CHONDROMA = "chondroma"
    OSTEOMA = "osteoma"
    HEMANGIOMA = "hemangioma"
    NEUROFIBROMA = "neurofibroma"
    LEIOMYOMA = "leiomyoma"
    RHABDOMYOMA = "rhabdomyoma"
    TERATOMA = "teratoma"
    GLIOMA = "glioma"
    SARCOMA = "sarcoma"
    CARCINOMA = "carcinoma"
    MELANOMA = "melanoma"
    LYMPHOMA = "lymphoma"
    MYELOMA = "myeloma"
    MESOTHELIOMA = "mesothelioma"
    BLASTOMA = "blastoma"

class TumorStateEnum(Enum):
    STAGE_0 = "stage_0"
    STAGE_I = "stage_I"
    STAGE_II = "stage_II"
    STAGE_III = "stage_III"
    STAGE_IV = "stage_IV"
    TIS = "Tis"
    T1 = "T1"
    T2 = "T2"
    T3 = "T3"
    T4 = "T4"
    N0 = "N0"
    N1 = "N1"
    N2 = "N2"
    N3 = "N3"
    M0 = "M0"
    M1 = "M1"
    G1 = "G1"
    G2 = "G2"
    G3 = "G3"
    G4 = "G4"
    LOW_GRADE = "low_grade"
    HIGH_GRADE = "high_grade"
    RECURRENT = "recurrent"
    PROGRESSIVE = "progressive"
    METASTATIC = "metastatic"
    IN_SITU = "in_situ"
    LOCALLY_ADVANCED = "locally_advanced"
    UNDIFFERENTIATED = "undifferentiated"
    DIFFERENTIATED = "differentiated"
    PRIMARY = "primary"
    SECONDARY = "secondary"
    PREMALIGNANT = "premalignant"
    MALIGNANT_BENIGN = "malignant_benign"
    TUMOR_IN_REGRESSION = "tumor_in_regression"
    REMISSION = "remission"
    RELAPSE = "relapse"
    PROLIFERATIVE = "proliferative"
    QUIESCENT = "quiescent"
    STABLE_DISEASE = "stable_disease"
    PARTIAL_RESPONSE = "partial_response"
    COMPLETE_RESPONSE = "complete_response"
    RAPIDLY_GROWING = "rapidly_growing"
    SLOWLY_GROWING = "slowly_growing"
    CHEMO_RESISTANT = "chemo_resistant"
    HORMONE_RESPONSIVE = "hormone_responsive"
    HORMONE_REFRACTORY = "hormone_refractory"
    RADIOSENSITIVE = "radiosensitive"
    RADIORESISTANT = "radioresistant"

class TumorSymptomEnum(Enum):
    PAIN = "pain"
    FATIGUE = "fatigue"
    WEIGHT_LOSS = "weight_loss"
    FEVER = "fever"
    NIGHT_SWEATS = "night_sweats"
    LOSS_OF_APPETITE = "loss_of_appetite"
    NAUSEA = "nausea"
    VOMITING = "vomiting"
    DIARRHEA = "diarrhea"
    CONSTIPATION = "constipation"
    ANEMIA = "anemia"
    SHORTNESS_OF_BREATH = "shortness_of_breath"
    COUGH = "cough"
    COUGHING_UP_BLOOD = "coughing_up_blood"
    CHEST_PAIN = "chest_pain"
    HEADACHE = "headache"
    VISION_CHANGES = "vision_changes"
    HEARING_CHANGES = "hearing_changes"
    SEIZURES = "seizures"
    MEMORY_LOSS = "memory_loss"
    CONFUSION = "confusion"
    DIZZINESS = "dizziness"
    WEAKNESS = "weakness"
    PARALYSIS = "paralysis"
    JOINT_PAIN = "joint_pain"
    BONE_PAIN = "bone_pain"
    SWELLING = "swelling"
    LYMPH_NODE_SWELLING = "lymph_node_swelling"
    ITCHING = "itching"
    SKIN_RASH = "skin_rash"
    BLEEDING = "bleeding"
    BRUISING = "bruising"
    JAUNDICE = "jaundice"
    ABDOMINAL_PAIN = "abdominal_pain"
    PELVIC_PAIN = "pelvic_pain"
    BACK_PAIN = "back_pain"
    URINARY_PROBLEMS = "urinary_problems"
    BLOOD_IN_URINE = "blood_in_urine"
    SEXUAL_DYSFUNCTION = "sexual_dysfunction"
    INFERTILITY = "infertility"
    DEPRESSION = "depression"
    ANXIETY = "anxiety"
    INSOMNIA = "insomnia"
    MOOD_SWINGS = "mood_swings"
    CHILLS = "chills"
    SWALLOWING_DIFFICULTY = "swallowing_difficulty"
    VOICE_CHANGES = "voice_changes"
    DRY_MOUTH = "dry_mouth"
    HAIR_LOSS = "hair_loss"
    BLOATING = "bloating"


class Tumor(BaseModel):
    organism_id: str = Field(..., description="ID of the parent organism")
    patient_ethnicity: List[EthnicityEnum] = Field(..., description="All ethnicities of the patient")
    tumor_type: TumorTypeEnum = Field(..., description="Type of the tumor")
    state: Optional[TumorStateEnum] = Field(..., description="State of the tumor")
    weight: Optional[float] = Field(..., description="Weight of the tumor in grams")
    weight_unit: Optional[str] = Field(..., description="Unit of the weight of the tumor")
    organism_status: Optional[str] = Field(..., description="Status of the parent organism")
    symptoms: List[TumorSymptomEnum] = Field(..., description="List of symptoms associated with the tumor")
    dimension_length_cm: Optional[float] = Field(..., description="Length of the tumor")
    dimension_width_cm: Optional[float] = Field(..., description="Width of the tumor")
    dimension_height_cm: Optional[float] = Field(..., description="Height of the tumor")
    growth_rate_mm_per_year: Optional[float] = Field(..., description="Growth rate of the tumor in mm/year")
    # growth_rate: Optional[Dict[str, Dict[str, float]]] = Field(
    #     ...,
    #     description="Growth rate of the tumor with unit and value combinations",
    #     example={"value": {"value": 2.5, "unit": "mm/year"}}
    # )
    age_of_patient: Optional[int] = Field(..., description="Age of the patient in years")
    gender_of_patient: Optional[str] = Field(..., description="Gender of the patient")
    tumor_location: Optional[str] = Field(..., description="Location of the tumor in the body")
    tumor_color: Optional[str] = Field(..., description="Color of the tumor")
    tumor_shape: Optional[str] = Field(..., description="Shape of the tumor")
    tumor_consistency: Optional[str] = Field(..., description="Consistency of the tumor")
    vascularity: Optional[str] = Field(..., description="Vascularity of the tumor")
    necrosis: Optional[bool] = Field(..., description="Presence of necrosis in the tumor")
    calcification: Optional[bool] = Field(..., description="Presence of calcification in the tumor")
    hemorrhage: Optional[bool] = Field(..., description="Presence of hemorrhage in the tumor")
    mitotic_rate: Optional[int] = Field(..., description="Mitotic rate of the tumor cells")
    tumor_border: Optional[str] = Field(..., description="Border characteristics of the tumor")
    genetic_mutations: Optional[List[str]] = Field(..., description="List of genetic mutations associated with the tumor")
    # tumor_marker_levels: Optional[Dict[str, Dict[str, float]]] = Field(
    #     ...,
    #     description="Tumor marker levels with unit and value combinations",
    #     example={"CEA": {"value": 3.5, "unit": "ng/mL"}, "CA19-9": {"value": 27, "unit": "U/mL"}}
    # )
    chemotherapy_response_date: Optional[date] = Field(..., description="Date of chemotherapy response")
    radiation_therapy_response_date: Optional[datetime] = Field(..., description="Datetime of radiation therapy response")
    immunotherapy_response_datetime: Optional[datetime] = Field(..., description="Datetime of immunotherapy response")
    surgery_status_date: Optional[date] = Field(..., description="Date of surgical intervention status")
    follow_up_interval_months: Optional[int] = Field(..., description="Follow-up interval for monitoring the tumor in months")
    clinical_trial_participation_date: Optional[datetime] = Field(..., description="Datetime of participation in clinical trials")
    patient_survival_rate: Optional[float] = Field(..., description="Survival rate of the patient in percentage")
    quality_of_life_score: Optional[float] = Field(..., description="Quality of life score of the patient")
    diagnosis_date: Optional[date] = Field(..., description="Date of tumor diagnosis")
    treatment_start_datetime: Optional[datetime] = Field(..., description="Datetime when treatment started")
    last_follow_up_datetime: Optional[datetime] = Field(..., description="Datetime of last follow-up")
    next_appointment_date: Optional[date] = Field(..., description="Date of next appointment")
    biopsy_date: Optional[date] = Field(..., description="Date of biopsy")
    genetic_testing_date: Optional[datetime] = Field(..., description="Datetime of genetic testing")
    last_treatment_update: Optional[datetime] = Field(..., description="Datetime of the last treatment update")
    




# Reagent
class PhysicalStateEnum(str, Enum):
    solid = "Solid"
    liquid = "Liquid"
    gas = "Gas"
    plasma = "Plasma"


class Reagent(ConfiguredBaseModel):
    reagent_name: str = Field(..., description="The name of the reagent")
    molecular_formula: Optional[str] = Field(..., description="The molecular formula of the reagent")
    molecular_weight_g_per_mol: Optional[float] = Field(..., description="The molecular weight of the reagent")
    physical_state: Optional[PhysicalStateEnum] = Field(
        ..., description="The physical state of the reagent at room temperature"
    )
    date_of_manufacture: Optional[datetime] = Field(..., description="The date when this reagent was created")
    expiration_date: Optional[datetime] = Field(..., description="The date when this reagent will expire")
