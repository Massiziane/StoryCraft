from typing import Optional
from datetime import datetime
from pydantic import BaseModel 

class StoryJobBase(BaseModel):
    theme: str

class StoryJobResponse(BaseModel):
    job_idL: int
    status: str
    created_at: datetime
    story_id: Optional[int] = None
    completed_at: Optional[datetime] = None
    error: Optional[str] = None

    class Config:
        from_attributes = True

# renaming this to StoryJobCreate for consistency with other schemas, even though it doesn't add any new fields for now. This allows for future expansion without breaking existing code.
class StoryJobCreate(StoryJobBase):
    pass



