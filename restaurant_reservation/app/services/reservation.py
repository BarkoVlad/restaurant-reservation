from datetime import datetime
from sqlalchemy.orm import Session
from ..models import reservation as models


def create_reservation(db: Session, reservation):
    db_reservation = models.Reservation(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation