from fastapi import APIRouter, Depends
from models.patient import  Patient
from typing import Optional, List
from bson import ObjectId     # type: ignore
from bson.errors import InvalidId # type: ignore
from fastapi import HTTPException
from db import patient_collection
from .utile import verify_token




router = APIRouter(
    dependencies=[Depends(verify_token)]
)


#-------------- Patient API ------------

@router.post("/patient/")
async def create_patient(patient_data: Patient):
    patient = patient_collection.insert_one(patient_data.dict())
    return {
        "message": "Patient Register successfully...!", 
        "id": str(patient.inserted_id)
    }
    
@router.get("/patients/")
async def get_all_patients():
    patients_cursor = patient_collection.find()
    patients = []
    for patient in patients_cursor:
        # print(str(patient["_id"]))
        patient["id"] = str(patient["_id"])  # Convert ObjectId to string
        del patient["_id"]

        patients.append(patient)
    return patients

@router.get("/patient/{patient_id}")
async def get_patient_by_id(patient_id: str):
    try:
        patient = patient_collection.find_one({"_id": ObjectId(patient_id)})
        if not patient:
            raise HTTPException(status_code=404, detail="Patient not found")
        
        # Convert ObjectId to string
        patient["id"] = str(patient["_id"])
        del patient["_id"]

        return patient

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid patient ID format")

@router.get("/patients/{registration_no}")
async def get_patient_by_registration_no(registration_no: str):
    patient = patient_collection.find_one({"registration_no": registration_no})
    if patient:
        patient["_id"] = str(patient["_id"])
        return patient
    return {"error": "Patient not found"}

@router.put("/patients/{patient_id}")
async def update_patient_by_id(patient_id: str, updated_data: Patient):
    try:
        obj_id = ObjectId(patient_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid patient ID")

    result = patient_collection.update_one(
        {"_id": obj_id},
        {"$set": updated_data.dict()}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    return {"message": "Patient details updated successfully"}

@router.delete("/patients/{patient_id}")
async def delete_patient_by_id(patient_id: str):
    try:
        obj_id = ObjectId(patient_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid patient ID")

    result = patient_collection.delete_one({"_id": obj_id})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    return {"message": "Patient deleted successfully"}

