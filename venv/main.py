from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from resume.routes import router as resume_router
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

# ✅ CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include router AFTER CORS and app definition
app.include_router(resume_router, prefix="/api")

# Optional direct endpoint for testing
@app.post("/api/resume/upload")
async def upload_resume(file: UploadFile = File(...)):
    contents = await file.read()
    return {"filename": file.filename, "size": len(contents)}
