from datetime import datetime
from typing import List

from sqlalchemy.orm import Session


from app.models.counter import Counter


def create_counter(db: Session, date: datetime):  # Accept datetime object directly
    try:
        new_counter = Counter(date=date)  # Use datetime directly
        db.add(new_counter)
        db.commit()
        db.refresh(new_counter)
        return new_counter
    except Exception as e:
        db.rollback()
        raise Exception(f"An error occurred while creating counter: {e}")


def get_counter(db: Session):
    return db.query(Counter).count()  # More efficient than len(db.query().all())
