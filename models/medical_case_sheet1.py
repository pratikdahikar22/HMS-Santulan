from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

#------------- Medical case sheet page 2 -------

class Drug(BaseModel):
    name: str
    age_of_first_use: int
    years_of_use: int
    years_of_excessive_use: int
    specific_type: str
    route_of_administration: str
    frequency_last_30_days: str
    quantities_last_30_days: str

class DrugCategory(BaseModel):
    drug_category: str
    drugs: List[Drug]

class DrinkingDrugHistory(BaseModel):
    patient_id: str
    name: str
    reg_no: str
    age: str
    date_of_registration: datetime
    drinking_drug_history: List[DrugCategory]


