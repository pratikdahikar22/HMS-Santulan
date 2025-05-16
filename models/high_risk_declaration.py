from typing import List, Optional
from pydantic import BaseModel



# ---------------- Personal & Family Background Model --------------------

class FamilyMember(BaseModel):
    name: Optional[str]
    age: Optional[str]
    education: Optional[str]
    occupation: Optional[str]
    income: Optional[str]
    health: Optional[str]
    relationship_with_patient: Optional[str]

class HighRiskDeclaration(BaseModel):
    history_of_suicide: bool
    history_of_psychiatric_illness: bool
    any_psychiatric_treatment: bool

class ChildhoodHistory(BaseModel):
    birth_history: Optional[str]
    developmental_milestones: Optional[str]
    school_performance: Optional[str]
    childhood_illnesses: Optional[str]
    relationship_with_peers: Optional[str]
    any_abuse_or_trauma: Optional[str]

class AdolescentHistory(BaseModel):
    emotional_behavioral_changes: Optional[str]
    social_relationships: Optional[str]
    academic_performance: Optional[str]

class PersonalFamilyBackground(BaseModel):
    patient_id: str
    high_risk_declaration: HighRiskDeclaration
    family_history: dict
    childhood_history: ChildhoodHistory
    adolescent_history: AdolescentHistory



# -------------- Marital, Educational, and Social History Model -------------------

class SpouseDetails(BaseModel):
    name: Optional[str]
    age: Optional[str]
    education: Optional[str]
    occupation: Optional[str]

class ChildrenDetails(BaseModel):
    name: Optional[str]
    age: Optional[str]
    education: Optional[str]
    health: Optional[str]
    behavior_issues: Optional[str]

class EducationalHistory(BaseModel):
    highest_education: Optional[str]
    academic_performance: Optional[str]
    difficulties_during_education: Optional[str]

class MaritalHistory(BaseModel):
    marital_status: Optional[str]
    age_at_marriage: Optional[str]
    duration_of_marriage: Optional[str]
    spouse_details: Optional[SpouseDetails]
    relationship_with_spouse: Optional[str]
    sexual_history: Optional[str]
    separation_divorce_details: Optional[str]

class FamilyViolenceHistory(BaseModel):
    emotional_abuse: bool
    physical_abuse: bool
    sexual_abuse: bool
    financial_abuse: bool
    details: Optional[str]

class AdjustmentPatterns(BaseModel):
    father: Optional[str]
    mother: Optional[str]
    siblings: Optional[str]
    spouse: Optional[str]
    children: Optional[str]

class MaritalEducationalSocialHistory(BaseModel):
    patient_id: str
    educational_history: EducationalHistory
    marital_history: MaritalHistory
    family_violence_history: FamilyViolenceHistory
    children_details: List[ChildrenDetails]
    adjustment_patterns: AdjustmentPatterns
    

# -------------------- Health & Psychological Profile Model --------------------

class HealthStatusOfFamily(BaseModel):
    chronic_illnesses: Optional[str]
    hereditary_conditions: Optional[str]
    mental_health_conditions: Optional[str]

class BehaviorProblems(BaseModel):
    aggression: bool
    withdrawal: bool
    substance_abuse: bool
    delinquency: bool
    suicidal_thoughts: bool
    self_harm: bool
    others: Optional[str]

class FamilyDamageSeenByCounsellor(BaseModel):
    emotional_damage: Optional[str]
    behavioral_issues: Optional[str]
    social_impact: Optional[str]
    counsellor_observations: Optional[str]

class HealthPsychologicalProfile(BaseModel):
    patient_id: str
    health_status_of_family: HealthStatusOfFamily
    behavior_problems: BehaviorProblems
    family_damage_seen_by_counsellor: FamilyDamageSeenByCounsellor
