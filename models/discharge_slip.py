from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date


class DepartmentClearance(BaseModel):
    department: str
    dept_head: Optional[str] = None
    remarks: Optional[str] = None
    sign: Optional[str] = None


class SecurityDetails(BaseModel):
    signature: Optional[str] = None
    time_out: Optional[str] = None  # format: "HH:MM"


class DischargeSlip(BaseModel):
    name: str
    registration_number: str = Field(..., alias="registration_number")
    doa: date  # Date of Admission
    dod: date  # Date of Discharge
    departmental_clearance: List[DepartmentClearance]
    counsellor_signature: Optional[str] = None
    project_coordinator_signature: Optional[str] = None
    security: Optional[SecurityDetails] = None
    final_acknowledgement: Optional[str] = None
    final_signature: Optional[str] = None
