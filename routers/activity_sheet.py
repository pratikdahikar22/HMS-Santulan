from fastapi import APIRouter,Depends
from models.activity_sheet import ActivitySheet 
from bson import ObjectId     # type: ignore
from bson.errors import InvalidId # type: ignore
from fastapi import HTTPException
from db import activity_sheet_collection
from .utile import verify_token


router = APIRouter(
    # dependencies = [Depends(verify_token)]
)


# ------------------- Activity Sheet --------------------

@router.post("/activity-sheet/")
async def create_activity_sheet(data:ActivitySheet):
    inserted_obj = activity_sheet_collection.insert_one(data.dict())

    return {
        'message': "Activity sheet created successfully...!",
        'id': str(inserted_obj.inserted_id)
    }
    
@router.get("/activity-sheet/")
async def get_activity_sheet_by_patient_id(patient_id: str):
    obj = activity_sheet_collection.find_one({'patient_id': patient_id})
    if not obj:
        raise HTTPException(status_code=400, detail="Activity sheet not found.")
    
    obj['id'] = str(obj['_id'])
    del obj['_id']
    
    return obj


@router.put("/activity-sheet/{id}")
async def update_activity_sheet(id: str, updated_data:ActivitySheet):
    try:
        obj_id = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail='Invalid activity sheet ID')
    
    result = activity_sheet_collection.update_one(
        {"_id": obj_id},
        {"$set": updated_data.dict()}        
    )
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Activity sheet not found")
    
    return {"message": "Activity sheet updated successfully"}
    