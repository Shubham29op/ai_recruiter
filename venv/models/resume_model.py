# models/resume_model.py

from sqlalchemy import Column, String, Integer, DateTime, JSON
from sqlalchemy.sql import func
from database import Base

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, index=True)
    file_url = Column(String)
    parsed_data = Column(JSON)
    score = Column(Integer)
    recommendations = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
