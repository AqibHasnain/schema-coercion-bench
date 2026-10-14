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





class Patient(ConfiguredBaseModel):
    species: str = Field(..., description="species of the patient")
    name: str = Field(..., description="Name of the patient")
    gender: Optional[str] = Field(None, description="Age of the patient")
    weight_kg: Optional[float] = Field(None, description="Weight of the patient in kg")
    active: Optional[bool] = Field(None, description="Active status of the patient")
    last_appointment_date: Optional[date] = Field(None, description="Date of the last appointment")
    ethnicity: Optional[List[EthnicityEnum]] = Field(None, description="All affiliated ethnicities of the patient")
    height_cm: Optional[float] = Field(None, description="Height of the patient in cm")
    blood_type: Optional[str] = Field(None, description="Blood type of the patient")
    allergies: Optional[str] = Field(None, description="Known allergies of the patient")
    chronic_conditions: Optional[str] = Field(None, description="Chronic conditions of the patient")
    emergency_contact_name: Optional[str] = Field(None, description="Name of the emergency contact")
    emergency_contact_phone: Optional[str] = Field(None, description="Phone number of the emergency contact")
    insurance_provider: Optional[str] = Field(None, description="Insurance provider of the patient")
    insurance_policy_number: Optional[str] = Field(None, description="Insurance policy number of the patient")
    address: Optional[str] = Field(None, description="Residential address of the patient")
    phone_number: Optional[str] = Field(None, description="Phone number of the patient")
    email: Optional[str] = Field(None, description="Email address of the patient")
    smoking_status: Optional[str] = Field(None, description="Smoking status of the patient")
    alcohol_consumption: Optional[str] = Field(None, description="Alcohol consumption level of the patient")
    medications: Optional[str] = Field(None, description="Current medications of the patient")
    family_history: Optional[str] = Field(None, description="Family medical history of the patient")

class Appointment(BaseModel):
    Appointment_ID: str = Field(..., description="Unique identifier for the appointment")
    patient: Patient = Field(..., description="Patient information")
    next_appointment_date: Optional[date] = Field(None, description="Date of next appointment")
    last_follow_up_datetime: Optional[datetime] = Field(None, description="Datetime of last follow-up")
    no_show: bool = Field(..., description="Whether the patient was a no-show for the appointment")
    appoint_made_type: str = Field(..., description="appointment made via website or phone")
    doctor_id: str = Field(..., description="Unique identifier for the doctor")
    department: str = Field(..., description="Department handling the appointment")
    reason_for_visit: str = Field(..., description="Reason for the appointment")
    treatment_plan: Optional[str] = Field(None, description="Planned treatment for the patient")
    treatment_notes: Optional[str] = Field(None, description="Notes on the treatment provided")
    prescription: Optional[str] = Field(None, description="Prescriptions given during the appointment")
    follow_up_instructions: Optional[str] = Field(None, description="Instructions for follow-up care")
    appointment_status: str = Field(..., description="Status of the appointment (e.g., scheduled, completed, canceled)")
    check_in_time: Optional[str] = Field(None, description="Time the patient checked in for the appointment")
    check_out_time: Optional[str] = Field(None, description="Time the patient checked out after the appointment")
    appointment_duration: Optional[int] = Field(None, description="Duration of the appointment in minutes")
    bill_amount: Optional[float] = Field(None, description="Total amount billed for the appointment")
    insurance_coverage: Optional[float] = Field(None, description="Amount covered by insurance")
    payment_status: str = Field(..., description="Status of the payment for the appointment")
    feedback: Optional[str] = Field(None, description="Patient feedback for the appointment")


