import uuid
from typing import Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Cookie, Response, BackgroundTasks
from sqlalchemy.orm import Session

from backend.db.database import get_db, SessionLocal
from backend.models.story import Story
from backend.models.job import StoryJob
from backend.schemas.story import (CompleteStoryNodeResponse, CreateStoryRequest, CompleteStoryResponse)
from backend.schemas.job import StoryJobResponse

router = APIRouter ( 
    prefix="/stories",
    tags=["stories"]
)


def get_session_id(session_id: Optional[str] = Cookie(None)):
    if not session_id:
        session_id = str(uuid.uuid4())
    return session_id

@router.post("/create", reponse_models=StoryJobResponse)
def create_story(
    request: CreateStoryRequest,
    background_tasks: BackgroundTasks,
    response: Response, 
    session_id: str = Depends(get_session_id),
    db: Session = Depends(get_db)
):
    response.set_cookie(key="session_id", values=session_id, httponly=True)

    job_id = str(uuid.uuid4())

    job = StoryJob(
        job_id=job_id,
        session_id=session_id,
        theme=request.theme,
        status="pending",
    )
    db.add(job)
    db.commit()

    background_tasks.add_task(
        generate_story_task,
        job_id=job_id,
        theme=request.theme,
        session_id=session_id
    )

    return job 

def generate_story_task(job_id: str, theme: str, session_id: str):
    db = SessionLocal()

    try:
        # query the first entry of the job from the database
        job = db.query(StoryJob).filter(StoryJob.job_id == job_id).first()


        if not job: 
            print(f"Job with id {job_id} not found")
            return
        
        try:
            job_status = "processing"
            db.commit()

            story = {} # TODO: generate story based on theme

            job.story_id = 1 # TODO: update story id
            job_status = "completed"
            job.completed_at = datetime.now()
            db.commit()
        except Exception as e:
            job_status = "failed"
            job.completed_at = datetime.now()
            job.error = str(e)
            db.commit()
    
    finally: 
        db.close()


@router.get("/{story_id}/complete", response_model=CompleteStoryResponse)
def get_complete_story(story_id: int, db: Session = Depends(get_db)):
    story = db.query(Story).filter(Story.id == story_id).first()
    if not story :
        raise HTTPException(status_code=404. detail="Story not found")
    
    complete_story = build_complete_story_tree(db, story)
    return story
    
def build_complete_story_tree(db: Session, story: Story) -> CompleteStoryNodeResponse:
    pass
 
