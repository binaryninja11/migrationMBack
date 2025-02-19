from enum import Enum
from typing import List, Dict, Union
from datetime import datetime

from pydantic import BaseModel


class SectionName(str, Enum):
    listing = "Аудирование"
    reading = "Чтение"
    writing = "Письмо"
    grammar = "Лексика и грамматика"
    history = "ИСТОРИЯ РОССИИ"
    low = "ОСНОВЫ ЗАКОНОДАТЕЛЬСТВА РОССИЙСКОЙ ФЕДЕРАЦИИ"



class Task(BaseModel):
    task_name : str
    header: str = None
    file_name: str = None
    body: str
    answers : List[str]


class Variant(BaseModel):
    variant_id: int
    body: List[Dict[SectionName, List[Task]]]

class Version(BaseModel):
    version_id: int

class DateGet(BaseModel):
    date: str

class DateSchema(BaseModel):
    date: datetime  # This will validate that the input is a valid date

    # class Config:
    #     json_encoders = {
    #         date: lambda v: v.isoformat()  # Ensures dates are serialized as ISO format (YYYY-MM-DD)
    #     }

class Counter(BaseModel):
    count: int

class AnswerResponse(BaseModel):
    answers: Dict[int, Union[int, str]]