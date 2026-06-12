"""Pydantic models for the drillhole API.

Two-model pattern (same as Rep 000):
  - DrillholeCreate: the request body for POST/PUT (no id, no logged_at — the DB
    assigns those).
  - Drillhole: the full response shape (everything, including DB-assigned fields).
"""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

Status = Literal["planned", "logging", "complete"]


class DrillholeCreate(BaseModel):
    hole_id: str
    status: Status
    rock_type: str
    grade: float = Field(ge=0)      # grade must be >= 0
    depth_m: float = Field(gt=0)    # depth must be > 0


class Drillhole(DrillholeCreate):
    id: int
    logged_at: datetime
