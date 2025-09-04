# 🤖 AI-Powered Resume & Job Assistant  

![Django](https://img.shields.io/badge/Django-5.x-green?logo=django)  
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)  
![PostgreSQL](https://img.shields.io/badge/Postgres-17-blue?logo=postgresql)  
![Render](https://img.shields.io/badge/Deployed%20on-Render-purple?logo=render)  

## 🔗 Live Demo  
👉 [AI Resume Assistant](https://ai-resume-assistant-1.onrender.com/)  

---

## 📌 Project Overview  
The **AI Resume & Job Assistant** is a Django-based web app that helps job seekers build, optimize, and analyze their resumes using **Google Gemini AI**.  

### ✨ Features  
- 📄 **AI Resume Builder**  
  - Generate resumes from a simple job description.  
  - Manual resume form with customization.  

- 🎤 **Interview Q&A Generator**  
  - Generates **technical + HR interview questions** based on your role, company, and resume.  
  - Provides **AI-suggested best answers** for practice.  

- 🎙 **Voice Assistant (Future Feature)**  
  - Ask: *"Make my resume stronger for a Data Analyst role"* and get instant improvements.  

- 📊 **Resume Analytics Dashboard**  
  - ATS readiness score (keyword density, structure).  
  - Skill distribution chart (Frontend, Backend, Data).  
  - Track number of resumes generated & downloaded.  

- 🛠 **Advanced Resume Features**  
  - Bullet point writer (AI generates professional work experience points).  
  - ATS optimizer (AI checks against job description).  
  - Rewrite suggestions (action verbs, quantified impact).  
  - Multiple resume styles (Modern, Minimal, Creative).  

---

## 🛠 Tech Stack  
- **Backend:** Django, Python  
- **Frontend:** HTML, CSS, Bootstrap, Chart.js  
- **Database:** PostgreSQL (on Render)  
- **AI Integration:** Google Gemini API  
- **Deployment:** Render (Web Service + Postgres)  

---

## ⚡ Installation & Setup  

### 1️⃣ Clone Repository
git clone https://github.com/Kunalgupta66/Ai-Resume-Assistant.git

2️⃣ Create Virtual Environment
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Setup Environment Variables

Create a .env file in the project root:

SECRET_KEY=your_django_secret_key
DEBUG=True
GEMINI_API_KEY=your_gemini_api_key

# Database (use PostgreSQL for deployment)
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

5️⃣ Run Migrations
python manage.py migrate
cd Ai-Resume-Assistantb.com/Kunalgupta66/Ai-Resume-Assistant.git
cd Ai-Resume-Assistant
