from fastapi import APIRouter
from models.discharge_slip import DischargeSlip
from typing import Optional, List
from bson import ObjectId     # type: ignore
from bson.errors import InvalidId # type: ignore
from fastapi import HTTPException
from db import discharge_slip_collection

router = APIRouter()



#-------------- Discharge slip API (page-15) -----------

@router.post("/discharge-slip/")
async def create_discharge_slip(data: DischargeSlip):
    inserted_obj = discharge_slip_collection.insert_one(data.dict())
    
    return {
        "message": "Discharge Slip details submitted successfully",
        "id": str(inserted_obj.inserted_id)
    }

@router.get("/discharge-slip/{patient_id}")
async def get_discharge_slip_by_patient_id(patient_id: str):
    try:
        obj = discharge_slip_collection.find_one({"patient_id": patient_id})
        if not obj:
            raise HTTPException(status_code=404, detail="Discharge Slip details not found")
        
        # Convert ObjectId to string
        obj["id"] = str(obj["_id"])
        del obj["_id"]

        return obj

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid Discharge Slip ID format")

@router.put("/discharge-slip/{id}")
async def update_discharge_slip_by_id(id: str, updated_data:DischargeSlip):
    try:
        obj_id = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid Discharge Slip ID")

    result = discharge_slip_collection.update_one(
        {"_id": obj_id},
        {"$set": updated_data.dict()}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Discharge Slip details not found")
    
    return {"message": "Discharge Slip details updated successfully"}


