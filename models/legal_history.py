from typing import Optional, List, Literal, Union
from pydantic import BaseModel


class DrugArrest(BaseModel):
    status: bool
    number_of_times: Optional[int] = 0


class LawIssue(BaseModel):
    type: str
    number_of_times: int
    description: Optional[str] = None


class LegalHistory(BaseModel):
    arrested_for_sale_of_drugs: DrugArrest
    arrested_for_possession_of_drugs: DrugArrest
    trouble_with_law: Optional[dict] = {
        "status": False,
        "issues": []
    }


class Activity(BaseModel):
    before_addiction: Union[bool, str]
    in_last_year: Union[bool, str]


class LeisureTimeActivities(BaseModel):
    playing_games: Activity
    going_to_movies: Activity
    watching_tv_or_music: Activity
    reading: Activity
    visiting_friends: Activity
    other_hobbies: Activity


class ReligiousPractices(BaseModel):
    pray_at_home: Literal["Always", "Sometimes", "Never"]
    visit_temple_regularly: Literal["Always", "Sometimes", "Never"]
    go_on_pilgrimages: Literal["Always", "Sometimes", "Never"]
    celebrate_festivals: Literal["Always", "Sometimes", "Never"]


class ReligiousBeliefs(BaseModel):
    identity: Literal["Believer", "Non believer", "Indifferent"]
    practices: ReligiousPractices


class PatientLegalHistory(BaseModel):
    patient_id: str
    legal_history: LegalHistory
    leisure_time_activities: LeisureTimeActivities
    religious_beliefs: ReligiousBeliefs
