from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    # Step 1 → AI description
    path("ai/description/", views.ai_description, name="ai_description"),
    path("ai/generate/", views.ai_generate, name="ai_generate"),  # POST

    # Step 2 → editable form
    path("resume/form/", views.resume_form, name="resume_form"),

    # Step 3 → preview + downloads
    path("resume/preview/", views.resume_preview, name="resume_preview"),
    path("resume/download/docx/", views.download_resume_docx, name="download_resume_docx"),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/register/", views.register, name="register"),
    path("download/<str:format>/", views.download_resume, name="download_resume"),
    path("interview-qna/", views.interview_qna, name="interview_qna"),



]
