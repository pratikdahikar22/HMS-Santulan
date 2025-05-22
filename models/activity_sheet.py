from pydantic import BaseModel
from typing import Optional, List, Dict


class Activity(BaseModel):
    date: str
    ic: str
    fc: str
    input1: str
    input2:str
    sign: str


class ActivitySheet(BaseModel):
    patient_id: str
    name: str
    doa: str
    reg_no: str
    activity: Optional[List[Activity]]
