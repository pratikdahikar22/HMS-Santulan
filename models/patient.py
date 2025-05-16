
from pydantic import BaseModel
from typing import Optional, List


    
#------------Patient Registration ------------

class LivingArrangements(BaseModel):
    live_with_family: bool
    live_with_friends_or_distant_relatives: bool
    live_alone: bool
    on_the_street: bool

class FamilyMemberGuardian(BaseModel):
    name: str
    address: str
    telephone_no: str

class ReferralSource(BaseModel):
    self: bool
    family: bool
    social_worker: bool
    physician: bool
    recovered_addict: bool
    employer: bool
    media: bool
    through_awareness_program: bool
    any_other: bool

class PriorTreatmentDetails(BaseModel):
    year: str
    place: str
    sobriety_duration: str

class Patient(BaseModel):
    # id: Optional[str] = None
    registration_no: str
    date_of_registration: str
    patient_name: str
    address: str
    telephone_no: str
    sex: str
    age: str
    date_of_birth: str
    religion: str
    community: str
    educational_qualification: str
    qualification_specify: str
    occupation: str
    income: str
    marital_status: str
    living_arrangements: LivingArrangements
    family_member_guardian: FamilyMemberGuardian
    referral_source: ReferralSource
    prior_treatment_for_addiction: str
    prior_treatment_details: PriorTreatmentDetails

