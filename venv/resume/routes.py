from fastapi import APIRouter, File, UploadFile, Form
from resume.parser import extract_text, parse_resume, score_resume
from resume.recommender import get_recommendations
from database import SessionLocal
from models.resume_model import Resume
import uuid

router = APIRouter()

@router.post("/resume/upload")
async def upload_resume(user_id: str = Form(...), file: UploadFile = File(...)):
    contents = await file.read()
    text = extract_text(contents, file.filename)

    parsed = parse_resume(text)
    score = score_resume(parsed)
    recommendations = get_recommendations(score)

    db = SessionLocal()
    resume = Resume(
        id=str(uuid.uuid4()),
        user_id=user_id,
        file_url="N/A",  # You can later upload to S3 or Supabase Storage
        parsed_data=parsed,
        score=score,
        recommendations=recommendations
    )
    db.add(resume)
    db.commit()
    db.refresh(resume)
    db.close()

    return {
        "score": score,
        "parsed": parsed,
        "recommendations": recommendations
    }
