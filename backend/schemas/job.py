from typing import List, Optional, Dictionary
from pydantic import BaseModel
from datetime import datetime

class StoryOptionasSchema(BaseModel):
    text: str
    node_id: Optional[int] = None


class StoryNodeBase(BaseModel):
    content: str
    is_ending: bool = False
    is_winning: bool = False


class CompleteStoryNodeResponse():
    id: int
    options: List(StoryOptionasSchema) = []

    class Config:
        from_attributes = True