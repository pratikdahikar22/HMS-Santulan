from typing import List, Optional
from pydantic import BaseModel
from datetime import date


class ReferralModel(BaseModel):
    date: Optional[date]
    details_of_visits: Optional[str]
    action_taken: Optional[str]
    referred_to: Optional[str]
    organisation_name: Optional[str]


class TreatmentGoal(BaseModel):
    goal: str
    specific_activities: Optional[str]
    time_frame: Optional[str]


class DropOutModel(BaseModel):
    date: Optional[date]
    reasons: List[str]


class ExtensionOfStayModel(BaseModel):
    reasons: Optional[str]


class ReferralAndTreatmentModel(BaseModel):
    patient_id: str
    referral: Optional[ReferralModel]
    treatment_plan: List[TreatmentGoal]
    drop_out: Optional[DropOutModel]
    extension_of_stay: Optional[ExtensionOfStayModel]
