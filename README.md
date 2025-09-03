# AI Resume Assistant

AI-powered resume & job assistant built with Django and Google Gemini (Generative AI).  
Features: AI resume generation, editable form, resume preview, exports, interview Q&A, analytics.

## Quick start (local)

1. Clone
```bash
git clone https://github.com/<YOUR_USERNAME>/<REPO>.git
cd <REPO>

2. Create venv & install

python -m venv .venv
source .venv/bin/activate   # mac/linux
.venv\Scripts\activate      # windows
pip install -r requirements.txt


3. Environment variables
Create a .env file (do NOT commit) and add:

DJANGO_SECRET_KEY=changeme
DEBUG=True
GEMINI_API_KEY=your_gemini_api_key
DATABASE_URL=sqlite:///db.sqlite3    # or your mysql/postgres URL
ALLOWED_HOSTS=localhost,127.0.0.1


4. Run migrations & start

python manage.py migrate
python manage.py runserver