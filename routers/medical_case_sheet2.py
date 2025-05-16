from fastapi import APIRouter
from models.medical_case_sheet2 import MedicalCaseShee2 
from typing import Optional, List
from bson import ObjectId     # type: ignore
from bson.errors import InvalidId # type: ignore
from fastapi import HTTPException
from db import medical_case_sheet2_collection

router = APIRouter()


# medical_case_sheet2_collection = database['medical_case_sheet2']


#-------------- Medical case sheet2 API (page-3) -----------

@router.post("/medical-case-sheet2/")
async def create_medical_case_sheet2(data: MedicalCaseShee2):
    inserted_obj = medical_case_sheet2_collection.insert_one(data.dict())
    
    return {
        "message": "Medical case sheet submitted successfully",
        "id": str(inserted_obj.inserted_id)
    }

@router.get("/medical-case-sheet2/{patient_id}")
async def get_medical_case_shee2t_by_patient_id(patient_id: str):
    try:
        obj = medical_case_sheet2_collection.find_one({"patient_id": patient_id})
        if not obj:
            raise HTTPException(status_code=404, detail="medical case sheet not found")
        
        # Convert ObjectId to string
        obj["id"] = str(obj["_id"])
        del obj["_id"]

        return obj

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid sheet ID format")

@router.put("/medical-case-sheet2/{id}")
async def update_medical_case_sheet2_by_id(id: str, updated_data:MedicalCaseShee2):
    try:
        obj_id = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid sheet ID")

    result = medical_case_sheet2_collection.update_one(
        {"_id": obj_id},
        {"$set": updated_data.dict()}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Medical case sheet not found")
    
    return {"message": "Medical case sheet updated successfully"}


