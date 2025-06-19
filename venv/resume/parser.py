import io
import pdfplumber
import docx
import re
import nltk

# Extract text from PDF or DOCX
def extract_text(file_bytes: bytes, filename: str) -> str:
    if filename.lower().endswith('.pdf'):
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)
    elif filename.lower().endswith('.docx'):
        doc = docx.Document(io.BytesIO(file_bytes))
        return "\n".join([para.text for para in doc.paragraphs])
    else:
        raise ValueError("Unsupported file format")

# Parse resume text to extract key info
def parse_resume(text: str) -> dict:
    name = extract_name(text)
    skills = extract_skills(text)
    experience = extract_experience(text)

    return {
        "name": name,
        "skills": skills,
        "experience": experience
    }

# Dummy name extractor (first capitalized sentence)
def extract_name(text: str) -> str:
    lines = text.strip().split("\n")
    for line in lines:
        if line and line[0].isupper() and len(line.split()) <= 4:
            return line.strip()
    return "Unknown"

# Example skill matcher (add more as needed)
def extract_skills(text: str) -> list:
    known_skills = [
        "python", "java", "c++", "sql", "fastapi", "django",
        "react", "node", "javascript", "aws", "docker", "html", "css"
    ]
    text_lower = text.lower()
    return [skill for skill in known_skills if skill in text_lower]

# Extract experience (naive match: e.g. "3 years", "2+ years")
def extract_experience(text: str) -> str:
    match = re.search(r"(\d+)\+?\s+years", text.lower())
    return match.group(0) if match else "Not mentioned"

# Score resume based on skills and experience
def score_resume(parsed: dict) -> int:
    skill_score = len(parsed["skills"]) * 10
    exp_match = re.search(r"\d+", parsed.get("experience", ""))
    exp_score = int(exp_match.group()) * 5 if exp_match else 0
    return min(skill_score + exp_score, 100)
