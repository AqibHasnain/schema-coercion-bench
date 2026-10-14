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

class Experiment(ConfiguredBaseModel):
    strain: str = Field(..., description="the strain of the microbe")
    crispr: str = Field(..., description="the gene name that was manipulated")
    timept_hrs: Optional[int] = Field(None, description="time point of sampling")
    media: Optional[str] = Field(None, description="media used for growth")
    carbon_source: Optional[str] = Field(None, description="carbon source used for growth")
    nitrogen_source: Optional[str] = Field(None, description="nitrogen source used for growth")
    stressor: Optional[str] = Field(None, description="stressor used for growth")
    shaking_speed: Optional[str] = Field(None, description="shaking speed in rpm")
    shaking_temp: Optional[str] = Field(None, description="shaking temperature in degrees C")
    plate_type: Optional[str] = Field(None, description="type of plate used for growth")
    
