from pydantic import BaseModel
from typing import Optional, List



#------------- Declaration Indemnity Form page 5 -------

class Applicant(BaseModel):
    name: Optional[str] = ""
    age: Optional[str] = ""
    residing_at: Optional[str] = ""
    declaration_place: Optional[str] = ""

class ParentGuardian(BaseModel):
    name: Optional[str] = ""
    age: Optional[str] = ""
    residing_at: Optional[str] = ""

class Confirmation(BaseModel):
    executed_on_day: Optional[str] = ""
    executed_on_month: Optional[str] = ""
    executed_on_year: Optional[str] = ""

class FinalDeclaration(BaseModel):
    place: Optional[str] = ""
    day: Optional[str] = ""
    month: Optional[str] = ""
    year: Optional[str] = ""

# class Signatures(BaseModel):
#     applicant_signature: Optional[str] = ""
#     applicant_signature_date: Optional[str] = ""
#     parent_guardian_1_signature: Optional[str] = ""
#     parent_guardian_1_date: Optional[str] = ""
#     parent_guardian_2_signature: Optional[str] = ""
#     parent_guardian_2_date: Optional[str] = ""

class DeclarationIndemnityForm(BaseModel):
    # id: Optional[str] = None
    patient_id: str
    project_in_charge: Optional[str] = "Santulan, Pune"
    applicant: Applicant
    parent_guardian: ParentGuardian
    confirmation: Confirmation
    final_declaration: FinalDeclaration
    # signatures: Signatures

