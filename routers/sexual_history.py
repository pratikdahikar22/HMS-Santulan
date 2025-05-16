from fastapi import APIRouter
from models.sexual_history import SexualHistory
from typing import Optional, List
from bson import ObjectId     # type: ignore
from bson.errors import InvalidId # type: ignore
from fastapi import HTTPException
from db import sexual_histroy_collection

router = APIRouter()



#-------------- Sexual History API (page-12) -----------

@router.post("/sexual-histroy/")
async def create_sexual_histroy(data: SexualHistory):
    inserted_obj = sexual_histroy_collection.insert_one(data.dict())
    
    return {
        "message": "Sexual History details submitted successfully",
        "id": str(inserted_obj.inserted_id)
    }

@router.get("/sexual-histroy/{patient_id}")
async def get_sexual_histroy_by_patient_id(patient_id: str):
    try:
        obj = sexual_histroy_collection.find_one({"patient_id": patient_id})
        if not obj:
            raise HTTPException(status_code=404, detail="Sexual History details not found")
        
        # Convert ObjectId to string
        obj["id"] = str(obj["_id"])
        del obj["_id"]

        return obj

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid Sexual History ID format")

@router.put("/sexual-histroy/{id}")
async def update_sexual_histroy_by_id(id: str, updated_data:SexualHistory):
    try:
        obj_id = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid Sexual History ID")

    result = sexual_histroy_collection.update_one(
        {"_id": obj_id},
        {"$set": updated_data.dict()}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Sexual History details not found")
    
    return {"message": "Sexual History details updated successfully"}


