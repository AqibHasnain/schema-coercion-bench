from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel, EmailStr, Field, conint
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

    Species: SpeciesEnum = Field(
        ..., description="""imported from benchling - no description?"""
    )
    # Sex: SexEnum = Field(..., description="""imported from benchling - no description?""")
    Strain: Optional[str] = Field(
        None, description="""imported from benchling - no description?"""
    )
    Age: Optional[float] = Field(
        None, description="""imported from benchling - no description?"""
    )
    # Age_Unit_(Weeks_Months_etc.): Optional[AgeUnitEnum] = Field(None, description="""imported from benchling - no description?""")
    Age_Unit: Optional[AgeUnitEnum] = Field(
        None, description="""imported from benchling - no description?"""
    )
    Line: Optional[str] = Field(
        None, description="""imported from benchling - no description?"""
    )
    Genotype: Optional[str] = Field(
        None, description="""imported from benchling - no description?"""
    )
    Phenotype: Optional[str] = Field(
        None, description="""imported from benchling - no description?"""
    )
    # Race: Optional[RaceEnum] = Field(None, description="""imported from benchling - no description?""")
    Ethnicity: Optional[List[EthnicityEnum]] = Field(
        default_factory=list,
        description="""imported from benchling - no description?""",
    )
    # Birth_Date: Optional[datetime ] = Field(None, description="""imported from benchling - no description?""")
    # Death_Date: Optional[datetime ] = Field(None, description="""imported from benchling - no description?""")
    Birth_Date: Optional[date] = Field(
        None, description="""imported from benchling - no description?"""
    )
    Death_Date: Optional[date] = Field(
        None, description="""imported from benchling - no description?"""
    )
    Health_Status: Optional[str] = Field(
        None, description="""imported from benchling - no description?"""
    )
    Comorbidities: Optional[str] = Field(
        None, description="""imported from benchling - no description?"""
    )
    Diet: Optional[str] = Field(
        None, description="""imported from benchling - no description?"""
    )
    # Randomized_/_Unrandomized: Optional[Randomize/UnrandomizedEnum] = Field(None, description="""imported from benchling - no description?""")
    Randomized___Unrandomized: Optional[Randomize_UnrandomizedEnum] = Field(
        None, description="""imported from benchling - no description?"""
    )
    Masking_ID: Optional[str] = Field(
        None, description="""imported from benchling - no description?"""
    )
    Physical_Tag: Optional[str] = Field(
        None, description="""imported from benchling - no description?"""
    )
    # Parent_Material_ID(s): Optional[str] = Field(None, description="""imported from benchling - no description?""")
    Parent_Material_ID_s_: Optional[str] = Field(
        None, description="""imported from benchling - no description?"""
    )
    has_Mother_ID: Optional[Organism] = Field(
        None, description="""imported from benchling - no description?"""
    )
    has_Father_ID: Optional[Organism] = Field(
        None, description="""imported from benchling - no description?"""
    )
    Mother_Lineage: Optional[str] = Field(
        None, description="""imported from benchling - no description?"""
    )
    Father_Lineage: Optional[str] = Field(
        None, description="""imported from benchling - no description?"""
    )
    Owner_User: Optional[str] = Field(
        None, description="""imported from benchling - no description?"""
    )
    System: Optional[str] = Field(
        None, description="""imported from benchling - no description?"""
    )
    System_id: Optional[str] = Field(
        None, description="""imported from benchling - no description?"""
    )
    organism_id: Optional[str] = Field(
        None, description="""imported from benchling - no description?"""
    )
    # Wean_Date: Optional[datetime ] = Field(None, description="""imported from benchling - no description?""")
    # Tail_Tag_Date: Optional[datetime ] = Field(None, description="""imported from benchling - no description?""")
    # Mature_Date: Optional[datetime ] = Field(None, description="""imported from benchling - no description?""")
    Wean_Date: Optional[date] = Field(
        None, description="""imported from benchling - no description?"""
    )
    Tail_Tag_Date: Optional[date] = Field(
        None, description="""imported from benchling - no description?"""
    )
    Mature_Date: Optional[date] = Field(
        None, description="""imported from benchling - no description?"""
    )
    Litter_SID: Optional[str] = Field(
        None, description="""imported from benchling - no description?"""
    )
    Mouseline: Optional[str] = Field(
        None, description="""imported from benchling - no description?"""
    )
    Notes: Optional[str] = Field(
        None, description="""imported from benchling - no description?"""
    )


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
    health_status: HealthStatusEnum = Field(
        ..., description="Health status of the organ"
    )
    organism_id: str = Field(..., description="ID of the parent organism")


# Experiment
class Experiment(ConfiguredBaseModel):
    lead_researcher_id: str = Field(..., description="ID of the lead researcher")
    start_date: Optional[datetime] = Field(
        ..., description="Start date of the experiment"
    )
    end_date: Optional[datetime] = Field(..., description="End date of the experiment")
    treatment_id: str = Field(..., description="ID of the treamtment")
    organism_id: str = Field(
        ..., description="ID of the organism"
    )  # This will eventually need to be a list


# Researcher
class Researcher(ConfiguredBaseModel):
    name: str = Field(..., description="Name of the researcher")
    role: str = Field(..., description="Role of the researcher")
    experiment_ids: Optional[List[str]] = Field(
        default_factory=list,
        description="The list of experiement_ids performed by the researcher.",
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
    infectious_agent_type: InfectiousAgentEnum = Field(
        ..., description="Agent of infection"
    )
    affected_system: BodySystemAgentEnum = Field(
        ..., description="The system in the body that is affected"
    )
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


# Tumor
class TumorTypeEnum(str, Enum):
    osteoma = "Osteoma"
    adenoma = "Adenoma"
    leukemia = "Leukemia"
    other = "Other"


class TumorStateEnum(str, Enum):
    benign = "Benign"
    malignant = "Malignant"
    other = "Other"


class Tumor(ConfiguredBaseModel):
    tumor_type: TumorTypeEnum = Field(..., description="Type of the tumor")
    state: Optional[TumorStateEnum] = Field(..., description="State of the tumor")
    weight: Optional[float] = Field(..., description="Weight of the tumor")
    organism_id: str = Field(..., description="ID of the parent organism")
    organism_status: Optional[str] = Field(
        ..., description="Status of the parent organism"
    )


# Reagent
class PhysicalStateEnum(str, Enum):
    solid = "Solid"
    liquid = "Liquid"
    gas = "Gas"
    plasma = "Plasma"


class Reagent(ConfiguredBaseModel):
    reagent_name: str = Field(..., description="The name of the reagent")
    molecular_formula: Optional[str] = Field(
        ..., description="The molecular formula of the reagent"
    )
    molecular_weight: Optional[float] = Field(
        ..., description="The molecular weight of the reagent"
    )
    physical_state: Optional[PhysicalStateEnum] = Field(
        ..., description="The physical state of the reagent at room temperature"
    )
    date_of_manufacture: Optional[datetime] = Field(
        ..., description="The date when this reagent was created"
    )
    expiration_date: Optional[datetime] = Field(
        ..., description="The date when this reagent will expire"
    )


# 1. User Model
class User(BaseModel):
    id: int
    name: str
    email: EmailStr


# 2. Address Model
class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str


# 3. Product Model
class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool


# 4. Order Model
class Order(BaseModel):
    order_id: int
    user_id: int
    product_ids: List[int]
    total_amount: float


# 5. Employee Model
class Employee(BaseModel):
    name: str
    age: int
    email: EmailStr
    department: str
    employee_id: str


# 6. Company Model
class Company(BaseModel):
    name: str
    address: Address
    employees: List[Employee]


# 7. BlogPost Model
class BlogPost(BaseModel):
    title: str
    content: str
    author: str
    published_at: datetime


# 8. Comment Model
class Comment(BaseModel):
    user: str
    content: str
    timestamp: datetime


# 9. Category Model
class Category(BaseModel):
    id: int
    name: str


# 10. Tag Model
class Tag(BaseModel):
    id: int
    name: str


# 11. Article Model
class Article(BaseModel):
    title: str
    content: str
    author: str
    categories: List[Category]
    tags: List[Tag]


# 12. Event Model
class Event(BaseModel):
    name: str
    location: str
    start_time: datetime
    end_time: datetime


# 13. Ticket Model
class Ticket(BaseModel):
    event_id: int
    user_id: int
    seat_number: str


# 14. Movie Model
class Movie(BaseModel):
    title: str
    director: str
    release_date: datetime
    genres: List[str]


# 15. Review Model
class Review(BaseModel):
    movie_id: int
    user_id: int
    rating: conint(ge=1, le=5)
    comment: Optional[str]


# 16. Book Model
class Book(BaseModel):
    title: str
    author: str
    published_date: datetime
    isbn: str


# 17. Library Model
class Library(BaseModel):
    name: str
    address: Address
    books: List[Book]


# 18. Course Model
class Course(BaseModel):
    course_id: str
    name: str
    description: str
    credits: int


# 19. Student Model
class Student(BaseModel):
    id: int
    name: str
    email: EmailStr
    courses: List[Course]


# 20. Teacher Model
class Teacher(BaseModel):
    id: int
    name: str
    email: EmailStr
    subjects: List[str]


# 21. School Model
class School(BaseModel):
    name: str
    address: Address
    students: List[Student]
    teachers: List[Teacher]


# 22. Vehicle Model
class Vehicle(BaseModel):
    make: str
    model: str
    year: int
    vin: str


# 23. Driver Model
class Driver(BaseModel):
    name: str
    license_number: str
    vehicles: List[Vehicle]


# 24. InsurancePolicy Model
class InsurancePolicy(BaseModel):
    policy_number: str
    holder: str
    start_date: datetime
    end_date: datetime
    coverage_amount: float


# 25. Claim Model
class Claim(BaseModel):
    claim_id: int
    policy_number: str
    amount: float
    date_filed: datetime


# 26. BankAccount Model
class BankAccount(BaseModel):
    account_number: str
    account_type: str
    balance: float


# 27. Transaction Model
class Transaction(BaseModel):
    transaction_id: int
    account_number: str
    amount: float
    transaction_date: datetime


# 28. Investment Model
class Investment(BaseModel):
    investment_id: int
    account_number: str
    type: str
    amount: float


# 29. Portfolio Model
class Portfolio(BaseModel):
    portfolio_id: int
    user_id: int
    investments: List[Investment]


# 30. Recipe Model
class Recipe(BaseModel):
    title: str
    ingredients: List[str]
    instructions: str


# 31. Ingredient Model
class Ingredient(BaseModel):
    name: str
    quantity: str


# 32. MealPlan Model
class MealPlan(BaseModel):
    name: str
    recipes: List[Recipe]


# 33. Workout Model
class Workout(BaseModel):
    name: str
    exercises: List[str]
    duration: int  # in minutes


# 34. Exercise Model
class Exercise(BaseModel):
    name: str
    sets: int
    reps: int


# 35. FitnessPlan Model
class FitnessPlan(BaseModel):
    name: str
    workouts: List[Workout]


# 36. Pet Model
class Pet(BaseModel):
    name: str
    species: str
    age: int


# 37. VetVisit Model
class VetVisit(BaseModel):
    pet_id: int
    date: datetime
    reason: str


# 38. Shelter Model
class Shelter(BaseModel):
    name: str
    address: Address
    pets: List[Pet]


# 39. Game Model
class Game(BaseModel):
    title: str
    genre: str
    release_date: datetime


# 40. Player Model
class Player(BaseModel):
    username: str
    email: EmailStr
    games: List[Game]


# 41. Team Model
class Team(BaseModel):
    name: str
    members: List[Player]


# 42. Tournament Model
class Tournament(BaseModel):
    name: str
    location: str
    date: datetime
    teams: List[Team]


# 43. MusicAlbum Model
class MusicAlbum(BaseModel):
    title: str
    artist: str
    release_date: datetime
    tracks: List[str]


# 44. Concert Model
class Concert(BaseModel):
    name: str
    location: str
    date: datetime
    performers: List[str]


# 45. Playlist Model
class Playlist(BaseModel):
    name: str
    songs: List[str]


# 46. Podcast Model
class Podcast(BaseModel):
    title: str
    host: str
    episodes: List[str]


# 47. Episode Model
class Episode(BaseModel):
    title: str
    duration: int  # in minutes
    release_date: datetime


# 48. Subscription Model
class Subscription(BaseModel):
    user_id: int
    service: str
    start_date: datetime
    end_date: Optional[datetime]


# 49. Newsletter Model
class Newsletter(BaseModel):
    title: str
    content: str
    subscribers: List[EmailStr]


# 50. Survey Model
class Survey(BaseModel):
    title: str
    questions: List[str]
    responses: List[dict]


# 51. Invoice Model
class Invoice(BaseModel):
    invoice_id: int
    customer_id: int
    amount_due: float
    due_date: datetime


# 52. Payment Model
class Payment(BaseModel):
    payment_id: int
    invoice_id: int
    amount: float
    payment_date: datetime


# 53. SubscriptionPlan Model
class SubscriptionPlan(BaseModel):
    plan_id: int
    name: str
    price: float
    duration_months: int


# 54. Membership Model
class Membership(BaseModel):
    user_id: int
    plan_id: int
    start_date: datetime
    end_date: Optional[datetime]


# 55. Task Model
class Task(BaseModel):
    task_id: int
    title: str
    description: str
    due_date: datetime
    completed: bool


# 56. Project Model
class Project(BaseModel):
    project_id: int
    name: str
    description: str
    tasks: List[Task]


# 57. Milestone Model
class Milestone(BaseModel):
    milestone_id: int
    project_id: int
    name: str
    due_date: datetime


# 58. BugReport Model
class BugReport(BaseModel):
    report_id: int
    project_id: int
    description: str
    reported_by: str
    status: str


# 59. FeatureRequest Model
class FeatureRequest(BaseModel):
    request_id: int
    project_id: int
    description: str
    requested_by: str
    status: str


# 60. Sprint Model
class Sprint(BaseModel):
    sprint_id: int
    project_id: int
    name: str
    start_date: datetime
    end_date: datetime


# 61. KanbanBoard Model
class KanbanBoard(BaseModel):
    board_id: int
    project_id: int
    name: str
    columns: List[str]


# 62. Column Model
class Column(BaseModel):
    column_id: int
    board_id: int
    name: str
    tasks: List[Task]


# 63. ChatMessage Model
class ChatMessage(BaseModel):
    message_id: int
    sender_id: int
    receiver_id: int
    content: str
    timestamp: datetime


# 64. ChatRoom Model
class ChatRoom(BaseModel):
    room_id: int
    name: str
    participants: List[int]
    messages: List[ChatMessage]


# 65. ForumPost Model
class ForumPost(BaseModel):
    post_id: int
    user_id: int
    title: str
    content: str
    timestamp: datetime


# 66. ForumThread Model
class ForumThread(BaseModel):
    thread_id: int
    title: str
    posts: List[ForumPost]


# 67. ForumCategory Model
class ForumCategory(BaseModel):
    category_id: int
    name: str
    threads: List[ForumThread]


# 68. Poll Model
class Poll(BaseModel):
    poll_id: int
    question: str
    options: List[str]
    votes: List[int]


# 69. Vote Model
class Vote(BaseModel):
    vote_id: int
    poll_id: int
    user_id: int
    option_index: int


# 70. Quiz Model
class Quiz(BaseModel):
    quiz_id: int
    title: str
    questions: List[str]
    answers: List[str]


# 71. Answer Model
class Answer(BaseModel):
    answer_id: int
    quiz_id: int
    user_id: int
    responses: List[str]


# 72. SurveyResponse Model
class SurveyResponse(BaseModel):
    response_id: int
    survey_id: int
    user_id: int
    answers: List[str]


# 73. Feedback Model
class Feedback(BaseModel):
    feedback_id: int
    user_id: int
    content: str
    timestamp: datetime


# 74. SupportTicket Model
class SupportTicket(BaseModel):
    ticket_id: int
    user_id: int
    issue: str
    state: str
    date_created: datetime


# 75. FAQ Model
class FAQ(BaseModel):
    question: str
    answer: str


# 76. KnowledgeBaseArticle Model
class KnowledgeBaseArticle(BaseModel):
    article_id: int
    title: str
    content: str
    tags: List[str]



# 77. Notification Model
class ReadCountEnum(str, Enum):
    High = "High"
    Medium = "Medium"
    Low = "Low"
class LocationEnum(str, Enum):
    HR = "HR"
    Finance = "Finance"
    IT = "IT"
    Marketing = "Marketing"
    Sales = "Sales"
class PermissionEnum(str, Enum): 
    Camera = "camera"
    Microphone = "microphone"
    Speaker = "speaker"    


class Notification(BaseModel):
    notification_id: int
    user_id: int
    message: str
    read: bool
    timestamp: datetime
    title: str
    priority: int
    to_user: str
    from_user: str
    url: str
    high_priority: bool
    category: str
    flagged: str
    importance: bool 
    read_count: Optional[ReadCountEnum]
    department: int
    location: Optional[LocationEnum] 
    updated_at: str
    schedule_time: str
    metadata: bool
    destination: str
    retry_count: str
    source: str
    status: str
    permissions: Optional[List[PermissionEnum]]





# 78. Alert Model
class Alert(BaseModel):
    alert_id: int
    type: str
    message: str
    timestamp: datetime


# 79. LogEntry Model
class LogEntry(BaseModel):
    log_id: int
    level: str
    log: str
    timestamp: datetime


# 80. AuditTrail Model
class AuditTrail(BaseModel):
    action_id: int
    user_id: int
    action: str
    timestamp: datetime


# 81. APIKey Model
class APIKey(BaseModel):
    key_id: int
    user_id: int
    key: str
    created_at: datetime


# 82. OAuthToken Model
class OAuthToken(BaseModel):
    token_id: int
    user_id: int
    token: str
    expires_at: datetime


# 83. Webhook Model
class Webhook(BaseModel):
    webhook_id: int
    url: str
    event: str
    created_at: datetime


# 84. Integration Model
class Integration(BaseModel):
    integration_id: int
    name: str
    settings: dict


# 85. Plugin Model
class Plugin(BaseModel):
    plugin_id: int
    name: str
    version: str
    settings: dict


# 86. Theme Model
class Theme(BaseModel):
    theme_id: int
    name: str
    settings: dict


# 87. Widget Model
class Widget(BaseModel):
    widget_id: int
    name: str
    settings: dict


# 88. Dashboard Model
class Dashboard(BaseModel):
    dashboard_id: int
    name: str
    widgets: List[Widget]


# 89. Report Model
class Report(BaseModel):
    report_id: int
    title: str
    content: str
    created_at: datetime


# 90. Metric Model
class Metric(BaseModel):
    metric_id: int
    name: str
    value: float
    timestamp: datetime


# 91. AnalyticsEvent Model
class AnalyticsEvent(BaseModel):
    event_id: int
    user_id: int
    event_type: str
    timestamp: datetime


# 92. Heatmap Model
class Heatmap(BaseModel):
    heatmap_id: int
    data: List[List[int]]
    timestamp: datetime


# 93. A/BTest Model
class ABTest(BaseModel):
    test_id: int
    name: str
    variants: List[str]
    results: List[float]


# 95. ResearchPaper Model
class ResearchPaper(BaseModel):
    paper_id: int
    title: str
    abstract: str
    authors: List[str]
    published_at: datetime


# 96. Citation Model
class Citation(BaseModel):
    citation_id: int
    paper_id: int
    cited_by: str
    citation_date: datetime


# 97. Patent Model
class Patent(BaseModel):
    patent_id: int
    title: str
    inventor: str
    filing_date: datetime
    grant_date: Optional[datetime]


# 98. Trademark Model
class Trademark(BaseModel):
    trademark_id: int
    name: str
    owner: str
    registration_date: datetime


# 99. License Model
class License(BaseModel):
    license_id: int
    name: str
    type: str
    issued_to: str
    issued_date: datetime
    expiration_date: Optional[datetime]


# 100. Certification Model
class Certification(BaseModel):
    certification_id: int
    name: str
    issued_by: str
    issued_date: datetime
    expiration_date: Optional[datetime]
