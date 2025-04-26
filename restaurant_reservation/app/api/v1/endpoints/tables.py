from fastapi import APIRouter

router = APIRouter(tags=["Tables"])

@router.get("/tables/")
def get_tables():
    return {"message": "Tables endpoint works!"}

@router.post("/tables/")
def create_table():
    return {"message": "Table created"}