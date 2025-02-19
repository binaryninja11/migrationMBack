from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Counter(Base):
    __tablename__ = "counter"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, unique=True, index=True, nullable=False)  # Removed format string


