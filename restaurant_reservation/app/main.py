from fastapi import FastAPI
from app.api.v1.endpoints import tables_router, reservations_router

app = FastAPI(title="Restaurant Reservation API")

app.include_router(tables_router, prefix="/api/v1")
app.include_router(reservations_router, prefix="/api/v1")

@app.get("/")
def health_check():
    return {"status": "ok", "message": "API is working"}