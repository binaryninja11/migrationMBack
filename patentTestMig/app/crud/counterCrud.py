from datetime import datetime
from typing import List

from sqlalchemy.orm import Session


from app.models.counter import Counter


def create_counter(db: Session, date: datetime):
    try:
        new_counter = Counter(date=date)
        db.add(new_counter)
        db.commit()
        db.refresh(new_counter)
        return new_counter
    except Exception as e:
        db.rollback()
        db.close()  # Ensure session is closed
        raise Exception(f"An error occurred while creating counter: {e}")


def get_counter(db: Session):
    count = db.query(Counter).count()
    return count if count is not None else 0  # Ensure it never returns None

