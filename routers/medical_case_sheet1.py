from fastapi import APIRouter
from models.medical_case_sheet1 import DrinkingDrugHistory
from typing import Optional, List
from bson import ObjectId     # type: ignore
from bson.errors import InvalidId # type: ignore
from fastapi import HTTPException
from db import drinking_drug_history_collection
from .utile import verify_token


router = APIRouter(
    # dependencies=[Depends(verify_token)]
)


# drinking_drug_history_collection = database['DrinkingDrugHistory']


#-------------- Medical case sheet API (page-2) -----------

@router.post("/medical-case-sheet/")
async def create_medical_case_sheet(data: DrinkingDrugHistory):
    inserted_obj = drinking_drug_history_collection.insert_one(data.dict())
    
    return {
        "message": "Medical case sheet submitted successfully",
        "id": str(inserted_obj.inserted_id)
    }

@router.get("/medical-case-sheet/{patient_id}")
async def get_medical_case_sheet_by_patient_id(patient_id: str):
    try:
        obj = drinking_drug_history_collection.find_one({"patient_id": patient_id})
        if not obj:
            raise HTTPException(status_code=404, detail="medical case sheet not found")
        
        # Convert ObjectId to string
        obj["id"] = str(obj["_id"])
        del obj["_id"]

        return obj

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid sheet ID format")

@router.put("/medical-case-sheet/{id}")
async def update_medical_case_sheet_by_id(id: str, updated_data:dict):
    try:
        obj_id = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid sheet ID")

    result = drinking_drug_history_collection.update_one(
        {"_id": obj_id},
        {"$set": updated_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Mecial case sheet not found")
    
    return {"message": "Medical case sheet updated successfully"}


