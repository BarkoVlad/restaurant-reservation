from fastapi import APIRouter

router = APIRouter()

@router.get("/reservations/")
def read_reservations():
    return {"message": "Reservations endpoint works!"}
