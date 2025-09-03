import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

SCHEMA_HINT = """
Return ONLY valid JSON. Keys: 
name, email, phone, location, summary,
skills: [{title, level}], 
education: [{degree, institute, start, end, score}],
experience: [{title, company, start, end, description}],
projects: [{name, tech, description}],
certifications: [{name, issuer, year}],
achievements: [string],
languages: [string],
interests: [string],
links: { github, linkedin, portfolio }
"""

def generate_structured_resume(description: str) -> dict:
    prompt = f"""
Generate a structured JSON resume.

For each job/project:
- Write 3–5 bullet points starting with action verbs (Developed, Designed, Led, Improved).
- Keep them ATS-friendly (no long paragraphs).
- Use concise, measurable achievements when possible.
    
You are a resume structuring assistant. Convert the following free-text description
into structured resume data. {SCHEMA_HINT}

Description:
\"\"\"{description}\"\"\"
"""
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        resp = model.generate_content(prompt)
        import json
        # Gemini sometimes wraps JSON in code fences; strip them.
        txt = resp.text.strip().strip("`")
        if txt.startswith("json"): txt = txt[4:].strip()
        data = json.loads(txt)
        # Minimal hardening
        data.setdefault("skills", [])
        data.setdefault("education", [])
        data.setdefault("experience", [])
        data.setdefault("projects", [])
        data.setdefault("certifications", [])
        data.setdefault("achievements", [])
        data.setdefault("languages", [])
        data.setdefault("interests", [])
        data.setdefault("links", {"github":"", "linkedin":"", "portfolio":""})
        return data
    except Exception:
        # Fallback skeleton if API fails
        return {
            "name": "", "email": "", "phone": "", "location": "", "summary": "",
            "skills": [], "education": [], "experience": [], "projects": [],
            "certifications": [], "achievements": [], "languages": [],
            "interests": [], "links": {"github":"", "linkedin":"", "portfolio":""}
        }



