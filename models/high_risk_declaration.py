from typing import List, Optional, Literal,Dict
from pydantic import BaseModel



# ------------- section 1 ----------------------

class HighRiskDeclarationForm(BaseModel):
    patient_id: str
    applicant_name: str
    applicant_signature: str
    applicant_signature_date: str
    parent_guardian_signature_1: Optional[str] = None
    parent_guardian_signature_date_1: Optional[str] = None
    parent_guardian_signature_2: Optional[str] = None
    parent_guardian_signature_date_2: Optional[str] = None

# ---------------section 2 ------------------------


class ParentDetails(BaseModel):
    name: str
    age: Optional[int]
    occupation: Optional[str]
    income: Optional[float]

class ParentalDeathInfo(BaseModel):
    # reason_for_death: Optional[str]
    age_at_time_of_death: Optional[int]

class SiblingInfo(BaseModel):
    relationship: str
    age: Optional[int]
    education: Optional[str]
    occupation: Optional[str]

class FamilyHistoryForm(BaseModel):
    patient_id: str
    father: ParentDetails
    mother: ParentDetails
    father_death_info: Optional[ParentalDeathInfo]
    mother_death_info: Optional[ParentalDeathInfo]
    siblings: List[SiblingInfo]
    
# --------------- section 3 --------------------

class ChildhoodExperience(BaseModel):
    poverty_or_severe_debt: Literal["Present", "Absent"]
    early_parental_loss: Literal["Present", "Absent"]
    extra_marital_affairs: Literal["Present", "Absent"]
    broken_home_single_parenting: Literal["Present", "Absent"]
    violence: Literal["Present", "Absent"]
    sexually_abused: Literal["Present", "Absent"]
    none: Literal["Present", "Absent"]
    any_other: Optional[str]

class BehaviorProblems(BaseModel):
    running_away_from_home: Optional[Literal["Present", "Absent"]]
    physical_fights_and_violence: Optional[Literal["Present", "Absent"]]
    destruction_of_property: Optional[Literal["Present", "Absent"]]
    stealing: Optional[Literal["Present", "Absent"]]
    scholastic_backwardness: Optional[Literal["Present", "Absent"]]
    experimenting_with_drugs_alcohol: Optional[Literal["Present", "Absent"]]
    gambling: Optional[Literal["Present", "Absent"]]
    any_other: Optional[str]
    
class ChildhoodAndAdolescent(BaseModel):
    patient_id: str
    childhood_description: Optional[str]
    childhood_experiences: ChildhoodExperience
    behavior_problems: BehaviorProblems

#-------------------Section 4 -------------------

class EducationalHistory(BaseModel):
    years_of_education: Optional[int]
    achievements_in_past: Optional[Literal["Present", "Absent"]]
    good_academic_records: Optional[Literal["Present", "Absent"]]
    high_achiever_in_extracurricular: Optional[Literal["Present", "Absent"]]

class SpouseDetails(BaseModel):
    name: str
    age: Optional[int]
    religion_or_community: Optional[str]
    education: Optional[str]
    occupation: Optional[str]
    income_per_month: Optional[float]
    # other_details: Optional[str]

class MaritalHistory(BaseModel):
    spouse: SpouseDetails
    marriage_type: Optional[Literal["Arranged", "Choice"]]
    accepted_by_family: Optional[bool]
    previous_or_subsequent_marriages: Optional[bool]
    separated_due_to_addiction: Optional[bool]
    longest_separation_period: Optional[str]
    
class Suspicion(BaseModel):
    under_influence: Optional[bool] = None
    while_abstinence: Optional[bool] = None
    
class ViolenceDetails(BaseModel):
    # is_patient_suspicious_of_wife: Suspicion
    is_patient_suspicious_of_wife: Optional[bool]
    under_influence: Optional[bool]
    while_abstinence: Optional[bool]
    family_violence: Optional[bool]
    family_violence_details: Optional[str]
    physical_violence_towards_family: Optional[bool]
    verbally_abusive: Optional[bool]
    violence_with_neighbors_or_outsiders: Optional[bool]
    breaking_articles_at_home: Optional[bool]

class ChildrenDetails(BaseModel):
    number_of_children: Optional[int]
    male: Optional[int]
    female: Optional[int]

class PatientHistory(BaseModel):
    patient_id: str
    education_histroy: EducationalHistory
    spouse_details: SpouseDetails
    marital_history: MaritalHistory
    violence_details: ViolenceDetails
    children_details: ChildrenDetails
    
#----------------section 5 -----------------------
class HealthStatusItem(BaseModel):
    problem: str
    parents_siblings_relation: Optional[str]
    parents_siblings_yes: Optional[bool]
    parents_siblings_no: Optional[bool]
    parents_siblings_dont_know: Optional[bool]
    
    wife_children_yes: Optional[bool]
    wife_children_relation: Optional[str]
    wife_children_no: Optional[bool]
    wife_children_dont_know: Optional[bool]

class familyConnection(BaseModel):
    parents: Optional[bool]  
    siblings: Optional[bool]  
    spouse: Optional[bool]  
    children: Optional[bool]  
    
class AdjustmentPatterns(BaseModel):
    no_family_dead: familyConnection  # keys: parents, siblings, spouse, children
    disowned_by_family: familyConnection
    mixed_or_indifferent: familyConnection
    minor_conflicts: familyConnection
    supportive: familyConnection
    not_applicable: familyConnection

class FamilyHealthStatus(BaseModel):
    patient_id: str
    health_status: List[HealthStatusItem]
    adjustment_patterns: AdjustmentPatterns
    family_damage_as_seen_by_counsellor: Optional[Literal["Mild", "Moderate", "Severe"]]



