from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date

class ApplicantInfo(BaseModel):
    name: str = Field(..., description="Name of the applicant (Parent or Guardian)")
    on_behalf_of: str = Field(..., description="Name of the person patient is being admitted for")
    relationship: str = Field(..., description="Relationship to the patient (e.g., Father, Mother, Husband, Wife)")

class PatientInfo(BaseModel):
    name: str = Field(..., description="Name of the patient")
    reason_for_admission: str = Field(..., description="Psychological reason for admission")

class PaymentInfo(BaseModel):
    monthly_general_fee_rs: float = Field(..., description="Monthly general ward fee")
    personal_expenditure_rs: float = Field(1000.0, description="Personal expenditure amount (default Rs.1000)")
    # psychiatric_consultation_rs: Optional[float] = Field(None, description="Monthly Psychiatric Consultation Fee")
    # psychiatric_medicine_required: Optional[bool] = False
    # general_medicine_required: Optional[bool] = False
    # family_counseling_required: Optional[bool] = False
    # pathological_tests_required: Optional[bool] = False
    # clothes_washing_required: Optional[bool] = False
    # special_diet_required: Optional[bool] = False
    # activities: Optional[List[str]] = Field(default_factory=list, description="List of additional activities (e.g., Picnic, Movie, Yoga)")
    # special_attendant_required: Optional[bool] = False

class DeclarationConsentForm(BaseModel):
    patient_id: str
    applicant_info: ApplicantInfo
    patient_info: PatientInfo
    payment_info: PaymentInfo
    understood_all_conditions: bool = Field(..., description="Has the applicant understood and agreed to all terms?")
    explained_in_local_language: Optional[bool] = Field(False, description="Was the form explained in Marathi/Hindi?")
    # applicant_signature: str = Field(..., description="Signature of the applicant")
    # applicant_signature_date: date
    # parent_guardian_signature: str = Field(..., description="Signature of parent or guardian")
    # parent_guardian_signature_date: date
    # second_guardian_signature: Optional[str] = Field(None, description="Signature of second guardian (if any)")
    # second_guardian_signature_date: Optional[date] = None
