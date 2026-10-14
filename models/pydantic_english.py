from __future__ import annotations 
from datetime import (
    datetime,
    date
)
from decimal import Decimal 
from enum import Enum 
import re
import sys
from typing import (
    Any,
    List,
    Literal,
    Dict,
    Optional,
    Union
)
from pydantic.version import VERSION  as PYDANTIC_VERSION 
if int(PYDANTIC_VERSION[0])>=2:
    from pydantic import (
        BaseModel,
        ConfigDict,
        Field,
        field_validator,
        AliasChoices
    )
else:
    from pydantic import (
        BaseModel,
        Field,
        validator
    )

class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
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

class Fixation_StorageTemperatureEnum(str, Enum):
    """
    imported from benchling - no description?
    """
    _20C = "-20C"
    _80C = "-80C"
    _150C = "-150C"
    number_4C = "4C"
    LN2 = "LN2"
    RT = "RT"

#class [Histo]FixativeUsedEnum(str, Enum):
class _Histo_FixativeUsedEnum(str, Enum):
    """
    imported from benchling - no description?
    """
    number_10PERCENT_SIGN_Zinc_Formalin = "10% Zinc Formalin"
    number_10PERCENT_SIGN_Neutral_Buffered_Formalin = "10% Neutral Buffered Formalin"
    number_4PERCENT_SIGN_Paraformaldehyde = "4% Paraformaldehyde"
    number_2PERCENT_SIGN_Paraformaldehyde = "2% Paraformaldehyde"
    Bouins = "Bouins"
    # None = "None"
    Other_LEFT_PARENTHESISPlease_IndicateRIGHT_PARENTHESIS = "Other (Please Indicate)"

class RaceEnum(str, Enum):
    """
    imported from benchling - no description?
    """
    American_Indian_or_alaska_native = "American Indian or alaska native"
    Asian = "Asian"
    Black_or_African_American = "Black or African American"
    Native_hawaiian_or_other_pacific_islander = "Native hawaiian or other pacific islander"
    White = "White"

# class Randomize/UnrandomizedEnum(str, Enum):
class Randomize_UnrandomizedEnum(str, Enum):
    """
    imported from benchling - no description?
    """
    Randomize = "Randomize"
    Unrandomized = "Unrandomized"

class SexEnum(str, Enum):
    """
    imported from benchling - no description?
    """
    Male = "Male"
    Female = "Female"
    NSOLIDUSA = "N/A"
    Unknown = "Unknown"

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
    #manual add
    Sus_domesticus = "Sus domesticus"

class TissueTypeEnum(str, Enum):
    """
    imported from benchling - no description?
    """
    Adipose = "Adipose"
    Adipose_tissue = "Adipose tissue"
    Adrenal_gland = "Adrenal gland"
    Aorta = "Aorta"
    Bladder = "Bladder"
    Blood_vessels = "Blood vessels"
    Bone = "Bone"
    Bone_marrow = "Bone marrow"
    Brain = "Brain"
    Breast = "Breast"
    Brown_adipose_tissue_LEFT_PARENTHESISBATRIGHT_PARENTHESIS = "Brown adipose tissue (BAT)"
    Brown_fat = "Brown fat"
    Cardiac_muscle = "Cardiac muscle"
    Cartilage = "Cartilage"
    Colon = "Colon"
    Cornea = "Cornea"
    Cortex = "Cortex"
    Dorsal_root_ganglia = "Dorsal root ganglia"
    Ear = "Ear"
    Esophagus = "Esophagus"
    Eye_LEFT_PARENTHESISretinaRIGHT_PARENTHESIS = "Eye (retina)"
    Fat___EpididymalSOLIDUSpariovanrian = "Fat - Epididymal/pariovanrian"
    Fat___retrorenal = "Fat - retrorenal"
    Fat___subcutaneous = "Fat - subcutaneous"
    Foreskin = "Foreskin"
    Gallbladder = "Gallbladder"
    Heart = "Heart"
    Hemibrain = "Hemibrain"
    Hippocampus = "Hippocampus"
    Hypothalamus = "Hypothalamus"
    Intestine = "Intestine"
    Kidney = "Kidney"
    Liver = "Liver"
    Lung = "Lung"
    Lung_F = "Lung F"
    Lymph_nodes = "Lymph nodes"
    Mammary_gland = "Mammary gland"
    Melanoma = "Melanoma"
    Mesenteric_lymph_node = "Mesenteric lymph node"
    Mucous_membranes = "Mucous membranes"
    Muscle = "Muscle"
    Muscle_LEFT_PARENTHESISskeletalRIGHT_PARENTHESIS = "Muscle (skeletal)"
    Muscle_LEFT_PARENTHESISsmoothRIGHT_PARENTHESIS = "Muscle (smooth)"
    Nerve = "Nerve"
    Nucleus_accumbens = "Nucleus accumbens"
    null = "null"
    Optic_nerve = "Optic nerve"
    Other = "Other"
    Ovary = "Ovary"
    Pancreas = "Pancreas"
    Parathyroid_gland = "Parathyroid gland"
    Peripheral_blood = "Peripheral blood"
    Pineal_gland = "Pineal gland"
    Pituitary = "Pituitary"
    Pituitary_gland = "Pituitary gland"
    Placenta = "Placenta"
    Prostate = "Prostate"
    Salivary_glands = "Salivary glands"
    Sciatic_Nerve = "Sciatic Nerve"
    Seminal_vesicles = "Seminal vesicles"
    Skin = "Skin"
    Small_intestine = "Small intestine"
    Spinal_cord = "Spinal cord"
    Spleen = "Spleen"
    Stomach = "Stomach"
    Submandibular_gland = "Submandibular gland"
    Substantia_nigra = "Substantia nigra"
    Tail = "Tail"
    Testis = "Testis"
    Thymus = "Thymus"
    Thyroid_gland = "Thyroid gland"
    Trachea = "Trachea"
    Tumor = "Tumor"
    Umbilical_cord = "Umbilical cord"
    Ureter = "Ureter"
    Uterus = "Uterus"
    White_adipose_tissue_LEFT_PARENTHESISWATRIGHT_PARENTHESIS = "White adipose tissue (WAT)"
    Whole_blood = "Whole blood"
    Fat = "Fat"
    Cecum = "Cecum"
    Cecal_content = "Cecal content"
    Mucosa = "Mucosa"
    Luminal_content = "Luminal content"
    #manual adds
    Adrenal = 'Adrenal'
    Cerebellum = 'Cerebellum'
    Eye = 'Eye'
    Femur_without_BM = 'Femur without BM'
    Frontal_cortex = 'Frontal cortex '
    Gall_bladder = 'Gall bladder'
    Large_intestine = 'Large intestine'
    LHS_Brain = 'LHS Brain'
    Midbrain = 'Midbrain'
    Olfactory_Bulb = 'Olfactory Bulb'
    Ovaries = 'Ovaries'
    Parietal_cortex = 'Parietal cortex'
    Skull_cap = 'Skull cap'
    Testes = 'Testes'
    Thyroid = 'Thyroid'
    Tongue = 'Tongue'
    Ulna_with_bone_marrow = 'Ulna with bone marrow'
    Ulna_without_bone_marrow = 'Ulna without bone marrow'

# class Yes/NoEnum(str, Enum):
class Yes_NoEnum(str, Enum):
    """
    imported from benchling - no description?
    """
    Yes = "Yes"
    No = "No"

class Organism(ConfiguredBaseModel):
    """
    imported from benchling - no description?
    """
    Species: SpeciesEnum = Field(..., description="""imported from benchling - no description?""")
    Sex: SexEnum = Field(..., description="""imported from benchling - no description?""")
    Strain: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Age: Optional[float] = Field(None, description="""imported from benchling - no description?""")
    # Age_Unit_(Weeks_Months_etc.): Optional[AgeUnitEnum] = Field(None, description="""imported from benchling - no description?""")
    Age_Unit: Optional[AgeUnitEnum] = Field(None, description="""imported from benchling - no description?""")
    Line: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Genotype: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Phenotype: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Race: Optional[RaceEnum] = Field(None, description="""imported from benchling - no description?""")
    Ethnicity: Optional[List[EthnicityEnum]] = Field(default_factory=list, description="""imported from benchling - no description?""")
    # Birth_Date: Optional[datetime ] = Field(None, description="""imported from benchling - no description?""")
    # Death_Date: Optional[datetime ] = Field(None, description="""imported from benchling - no description?""")
    Birth_Date: Optional[date] = Field(None, description="""imported from benchling - no description?""")
    Death_Date: Optional[date] = Field(None, description="""imported from benchling - no description?""")
    Health_Status: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Comorbidities: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Diet: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    # Randomized_/_Unrandomized: Optional[Randomize/UnrandomizedEnum] = Field(None, description="""imported from benchling - no description?""")
    Randomized___Unrandomized: Optional[Randomize_UnrandomizedEnum] = Field(None, description="""imported from benchling - no description?""")
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

class ProteomicsSample(ConfiguredBaseModel):
    """
    imported from benchling - no description?
    """
    has_Source_Sample: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Additional_Sample_Name: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Sample_Type: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    # has_Request_ID: Optional[[MassSpec]Request] = Field(None, description="""imported from benchling - no description?""")
    has_Request_ID: Optional[_MassSpec_Request] = Field(None, description="""imported from benchling - no description?""")
    # Species(human_mouse_rat): str = Field(..., description="""imported from benchling - no description?""")
    Species_human_mouse_rat_: str = Field(..., description="""imported from benchling - no description?""")
    Sex: SexEnum = Field(..., description="""imported from benchling - no description?""")
    # Tissue_or_Biofluid_Type_(e.g._Liver_Muscle_Brain_Blood_Plasma_Serum_Urine_Saliva): Optional[str] = Field(None, description="""imported from benchling - no description?""")
    # Tissue_Sub_type_(e.g_Hypothalamus_Hippocampus): Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Tissue_or_Biofluid_Type__e_g__Liver_Muscle_Brain_Blood_Plasma_Serum_Urine_Saliva_: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Tissue_Sub_type__e_g_Hypothalamus_Hippocampus_: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    #manual adds
    Benchling_Experiment_Design_Entry_ID__EXP______: Optional[str] = Field(None)
    Age: Optional[float] = Field(None, description="""imported from benchling - no description?""")
    Age_Unit: Optional[AgeUnitEnum] = Field(None, description="""imported from benchling - no description?""")
    Perturbation: Optional[str]=Field(None)

class Tissue(ConfiguredBaseModel):
    """
    imported from benchling - no description?
    """
    Alias: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    # has_Parent_Organism_ID: Organism = Field(..., description="""imported from benchling - no description?""")
    has_Parent_Organism_ID: str = Field(..., description="""imported from benchling - no description?""")
    Tissue_Type: TissueTypeEnum = Field(..., description="""imported from benchling - no description?""")
    # Date_of_Collection: datetime  = Field(..., description="""imported from benchling - no description?""")
    Date_of_Collection: date  = Field(..., description="""imported from benchling - no description?""")
    # has_[Optional]_Parent_Organ_ID: Optional[Organ] = Field(None, description="""imported from benchling - no description?""")
    has__Optional__Parent_Organ_ID: Optional[Organ] = Field(None, description="""imported from benchling - no description?""")
    Donor_Sex: Optional[SexEnum] = Field(None, description="""imported from benchling - no description?""")
    Donor_Species: Optional[SpeciesEnum] = Field(None, description="""imported from benchling - no description?""")
    # Age_of_Donor_(months): Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Age_of_Donor__months: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    # Fixative_Used: Optional[[Histo]FixativeUsedEnum] = Field(None, description="""imported from benchling - no description?""")
    Fixative_Used: Optional[_Histo_FixativeUsedEnum] = Field(None, description="""imported from benchling - no description?""")
    Total_Fixation_Time: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    # Fixation_temperature_(C): Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Fixation_temperature__C_: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    # Perfused?: Optional[Yes/NoEnum] = Field(None, description="""imported from benchling - no description?""")
    Perfused_: Optional[Yes_NoEnum] = Field(None, description="""imported from benchling - no description?""")
    Perfused_With: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Anatomical_Sub_Region: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    # Notes_/_Comments: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Notes___Comments: Optional[str] = Field(None, description="""imported from benchling - no description?""")
    # Sex_(c.f.): Optional[List[SexEnum]] = Field(None, description="""imported from benchling - no description?""")
    Sex: Optional[List[SexEnum]] = Field(None, description="""imported from benchling - no description?""")
    # Species_(c.f): Optional[List[SpeciesEnum]] = Field(None, description="""imported from benchling - no description?""")
    Species: Optional[List[SpeciesEnum]] = Field(None, description="""imported from benchling - no description?""")
    # has_Histology_Request: Optional[[Histology]RequestID] = Field(None, description="""imported from benchling - no description?""")
    has_Histology_Request: Optional[_Histology_RequestID] = Field(None, description="""imported from benchling - no description?""")


class Organ(ConfiguredBaseModel):
    """
    dummy class
    """
    pass

class _Histology_RequestID(ConfiguredBaseModel):
# class [Histology]RequestID(ConfiguredBaseModel):
    """
    dummy class
    """
    pass

# class [MassSpec]Request(ConfiguredBaseModel):
class _MassSpec_Request(ConfiguredBaseModel):
    """
    dummy class
    """
    pass



####eveerything after this was added manually for the synthetic dataset
class FailureDetectionEnum(str, Enum):
    """
    imported from benchling - no description?
    """
    foo = 'foo'
    bar = 'bar'

class DiseaseEnum(str, Enum):
    """
    imported from benchling - no description?
    """
    Actinobacillosis = 'Actinobacillosis'
    Aleutian_Mink_Disease = 'Aleutian Mink Disease'
    Anal_Gland_Neoplasms = 'Anal Gland Neoplasms'
    Anaplasmosis = 'Anaplasmosis'
    Bird_Diseases_ = 'Bird Diseases'
    Borna_Disease = 'Borna Disease'
    Cat_Diseases_ = 'Cat Diseases'
    Cattle_Diseases_ = 'Cattle Diseases'
    Digital_Dermatitis = 'Digital Dermatitis'
    Disease_Models_Animal = 'Disease Models Animal'
    Dog_Diseases_ = 'Dog Diseases'
    Enterotoxemia = 'Enterotoxemia'
    Erysipelothrix_Infections_ = 'Erysipelothrix Infections'
    Fish_Diseases_ = 'Fish Diseases'
    Foot_and_Mouth_Disease = 'Foot-and-Mouth Disease'
    Foot_Rot = 'Foot Rot'
    Goat_Diseases = 'Goat Diseases'
    Heartwater_Disease = 'Heartwater Disease'
    Hepatitis_Animal_ = 'Hepatitis Animal'
    Horse_Diseases_ = 'Horse Diseases'
    Keratoconjunctivitis_Infectious = 'Keratoconjunctivitis Infectious'
    Lameness_Animal = 'Lameness Animal'
    Mammary_Neoplasms_Animal = 'Mammary Neoplasms Animal'
    Mink_Viral_Enteritis = 'Mink Viral Enteritis'
    Muscular_Dystrophy_Animal_ = 'Muscular Dystrophy Animal'
    Myxomatosis_Infectious = 'Myxomatosis Infectious'
    Parasitic_Diseases_Animal_ = 'Parasitic Diseases Animal'
    Paratuberculosis = 'Paratuberculosis'
    Parturient_Paresis = 'Parturient Paresis'
    Peste_des_Petits_Ruminants = 'Peste-des-Petits-Ruminants'
    Pleuropneumonia_Contagious = 'Pleuropneumonia Contagious'
    Primate_Diseases_ = 'Primate Diseases'
    Pseudorabies = 'Pseudorabies'
    Pythiosis = 'Pythiosis'
    Rinderpest = 'Rinderpest'
    Rodent_Diseases_ = 'Rodent Diseases'
    Salmonella_Infections_Animal = 'Salmonella Infections Animal'
    Sheep_Diseases_ = 'Sheep Diseases'
    Steatitis = 'Steatitis'
    Swine_Diseases_ = 'Swine Diseases'
    Venereal_Tumors_Veterinary = 'Venereal Tumors Veterinary'
    Vesicular_Stomatitis = 'Vesicular Stomatitis'
    Wasting_Disease_Chronic = 'Wasting Disease Chronic'
    Zoonoses = 'Zoonoses'
    Arrhythmia_Sinus_ = 'Arrhythmia Sinus'
    Atrial_Fibrillation = 'Atrial Fibrillation'
    Atrial_Flutter = 'Atrial Flutter'
    Bradycardia = 'Bradycardia'
    Brugada_Syndrome = 'Brugada Syndrome'
    Cardiac_Complexes_Premature_ = 'Cardiac Complexes Premature'
    Commotio_Cordis = 'Commotio Cordis'
    Heart_Block_ = 'Heart Block'
    Long_QT_Syndrome_ = 'Long QT Syndrome'
    Parasystole = 'Parasystole'
    Pre_Excitation_Syndromes_ = 'Pre-Excitation Syndromes'
    Tachycardia_ = 'Tachycardia'
    Ventricular_Fibrillation = 'Ventricular Fibrillation'
    Ventricular_Flutter = 'Ventricular Flutter'
    Neoplasms = 'Neoplasms'
    Carcinoma = 'Carcinoma'
    No_disease = "No disease"

class Synthetic(ConfiguredBaseModel):
    """
    imported from benchling - no description?
    """
    Water_Temp__celsius_:Optional[str] = Field(...)
    Body_Mass__pounds_:Optional[str] =Field(...)
    Age:Optional[str] = Field(...)
    Age_Unit:Optional[AgeUnitEnum] = Field(...)
    Perturbation_1:Optional[str] = Field(...)
    Perturbation_2:Optional[str] = Field(...)
    Food_Mass__kg_:Optional[str] = Field(...)
    Disease: Optional[DiseaseEnum] = Field(...)
    Species:Optional[SpeciesEnum] = Field(...)
    Lint_Me:Optional[str] = Field(...)
    Experiment_Date:Optional[datetime] = Field(...)
    failure_detection_test:Optional[FailureDetectionEnum] = Field(...)
    diet: Optional[str] = Field(...)