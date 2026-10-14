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

class Strain(ConfiguredBaseModel):
    strain: str = Field(..., description="the strain of the microbe")
    gene_manipulated: str = Field(..., description="the gene name that was manipulated")
    timept_hrs: Optional[int] = Field(None, description="time point of sampling")