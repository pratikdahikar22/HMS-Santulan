from fastapi import APIRouter
from models.periodic_checkup import PeriodicCheckupChart
from typing import Optional, List
from bson import ObjectId     # type: ignore
from bson.errors import InvalidId # type: ignore
from fastapi import HTTPException
from db import periodic_checkup_collection

router = APIRouter()

# periodic_checkup_collection = database['PeriodicCheckup']



# -------------Periodically Checkup Chart page-4 --------------

@router.post("/periodic-checkup/")
async def create_periodic_checkup_chart(data: PeriodicCheckupChart):
    inserted_obj = periodic_checkup_collection.insert_one(data.dict())
    
    return {
        "message": "Periodic checkup data submitted successfully",
        "id": str(inserted_obj.inserted_id)
    }

@router.get("/periodic-checkup/{patient_id}")
async def get_periodic_checkup_chart_by_patient_id(patient_id: str):
    try:
        obj = periodic_checkup_collection.find_one({"patient_id": patient_id})
        if not obj:
            raise HTTPException(status_code=404, detail="Periodic Checkup chart not found")
        
        # Convert ObjectId to string
        obj["id"] = str(obj["_id"])
        del obj["_id"]

        return obj

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid Periodic Checkup ID format")

@router.put("/periodic-checkup/{id}")
async def update_periodic_checkup_chart_by_id(id: str, updated_data:PeriodicCheckupChart):
    try:
        obj_id = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid sheet ID")

    result = periodic_checkup_collection.update_one(
        {"_id": obj_id},
        {"$set": updated_data.dict()}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Periodic checkup not found")
    
    return {"message": "Periodic Checkup Chart updated successfully"}




