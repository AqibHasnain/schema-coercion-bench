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

# class Randomize/UnrandomizedEnum(str, Enum):
class ColorEnum(str, Enum):
    """
    imported from benchling - no description?
    """
    red = "red"
    orange = "orange"
    #no yellow
    green = "green"
    blue = "blue"
    purple = "purple"

class Synthetic(ConfiguredBaseModel):
    """
    imported from benchling - no description?
    """
    perturbation_1:Optional[str] = Field(...)
    perturbation_2:Optional[str] = Field(...)
    cube_volume__nm_:Optional[float] = Field(...)
    age__days_:Optional[float] = Field(...)
    protein_mass:Optional[float] = Field(...)
    protein_mass_unit:Optional[str] = Field(...)
    drug_volume__mL_:Optional[float] = Field(...)
    disease: Optional[DiseaseEnum] = Field(...)
    species: Optional[SpeciesEnum] = Field(...)
    color: Optional[ColorEnum] = Field(...)
    non_indicative_name: Optional[str] = Field(...)
    experiment_date:Optional[datetime] = Field(...)
    test_date:Optional[datetime] = Field(...)
    injection_date:Optional[datetime] = Field(...)
    shoe_brand:Optional[str] = Field(...)
