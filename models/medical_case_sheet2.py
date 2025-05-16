from pydantic import BaseModel, Field
from typing import List, Optional


class PhysicalExamination(BaseModel):
    pulse_rate: Optional[str] = ""
    urine_sugar: Optional[str] = ""
    blood_pressure: Optional[str] = ""
    weight: Optional[str] = ""
    tremors: bool = False
    lymph: bool = False
    glossitis: bool = False
    flushed_face: bool = False
    excessive_sweating: bool = False
    palmar_erythema: bool = False
    pedal_edema: bool = False
    injection_mark: bool = False
    jaundice: bool = False
    loss_of_body_hair: bool = False
    wasting_of_muscles: bool = False
    abcess: bool = False
    malnutrition: bool = False
    clubbing_of_nails: bool = False
    spider_naevii: bool = False
    anemia: bool = False
    gynaecomstia: bool = False


class SystemExaminationAbnormalities(BaseModel):
    respiratory_system: Optional[str] = ""
    cardio_vascular_system: Optional[str] = ""
    gastro_intestinal_system: Optional[str] = ""
    nervous_system: Optional[str] = ""


class MedicationEntry(BaseModel):
    date_month: Optional[str] = ""
    complaints: Optional[str] = ""
    medication: Optional[str] = ""
    reason_for_change: Optional[str] = ""
    signed_by_physician: Optional[str] = ""


class UntowardIncident(BaseModel):
    occurred: bool = False
    action_taken: Optional[str] = ""


class NeedOfReferral(BaseModel):
    medical: bool = False
    physical_problem: bool = False


class ReferralInfo(BaseModel):
    referred: bool = False
    date_of_referral: Optional[str] = ""
    need_of_referral: NeedOfReferral = NeedOfReferral()
    institution_name: Optional[str] = ""


class LastSubstanceUse(BaseModel):
    days_ago: Optional[str] = ""


class MedicalCaseShee2(BaseModel):
    patient_id: str
    physical_examination: PhysicalExamination
    system_examination_abnormalities: SystemExaminationAbnormalities
    medication_during_treatment: List[MedicationEntry] = []
    untoward_incident: UntowardIncident
    referral_info: ReferralInfo
    last_drink_or_drugs_taken: LastSubstanceUse
    diagnosis: Optional[str] = ""
