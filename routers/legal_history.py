from fastapi import APIRouter
from models.legal_history import PatientLegalHistory
from typing import Optional, List
from bson import ObjectId     # type: ignore
from bson.errors import InvalidId # type: ignore
from fastapi import HTTPException
from db import legal_histroy_collection

router = APIRouter()



#-------------- Legal History API (page-13) -----------

@router.post("/legal-histroy/")
async def create_legal_histroy(data: PatientLegalHistory):
    inserted_obj = legal_histroy_collection.insert_one(data.dict())
    
    return {
        "message": "Legal History details submitted successfully",
        "id": str(inserted_obj.inserted_id)
    }

@router.get("/legal-histroy/{patient_id}")
async def get_legal_histroy_by_patient_id(patient_id: str):
    try:
        obj = legal_histroy_collection.find_one({"patient_id": patient_id})
        if not obj:
            raise HTTPException(status_code=404, detail="Legal History details not found")
        
        # Convert ObjectId to string
        obj["id"] = str(obj["_id"])
        del obj["_id"]

        return obj

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid Legal History ID format")

@router.put("/legal-histroy/{id}")
async def update_legal_histroy_by_id(id: str, updated_data:PatientLegalHistory):
    try:
        obj_id = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid Legal History ID")

    result = legal_histroy_collection.update_one(
        {"_id": obj_id},
        {"$set": updated_data.dict()}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Legal History details not found")
    
    return {"message": "Legal History details updated successfully"}



