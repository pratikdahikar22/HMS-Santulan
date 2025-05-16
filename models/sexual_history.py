from typing import Optional, List, Literal
from pydantic import BaseModel


class ChildrenDetails(BaseModel):
    has_children: bool
    details: Optional[str] = None  # e.g., "One child aged 3"


class SexActivityDetail(BaseModel):
    involved: bool
    condom_usage: Optional[Literal["Always", "Sometimes", "Never"]] = None


class HIVTest(BaseModel):
    tested: bool
    result: Optional[Literal[
        "Positive",
        "Negative",
        "Not willing to reveal",
        "Not collected reports",
        "Not applicable"
    ]] = None


class SexualProblems(BaseModel):
    has_problems: bool
    issues: Optional[List[Literal[
        "Reduced libido",
        "Impotency",
        "Excessive sexual urge",
        "Complete abstinence"
    ]]] = None
    other: Optional[str] = None


class SexualHistory(BaseModel):
    patient_id: str
    extra_marital_experience: Literal["Present", "Absent", "N/A"]
    marital_status: Literal["Married", "Unmarried"]
    age_of_partner: Optional[int] = None
    sustained_relationship: Optional[bool] = None
    years_known_each_other: Optional[int] = None
    living_arrangement: Optional[str] = None
    any_children: ChildrenDetails
    high_risk_sexual_activities: bool
    commercial_sex_workers: SexActivityDetail
    casual_sexual_partners: SexActivityDetail
    hiv_test: HIVTest
    current_sexual_problems: SexualProblems


