from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    education = models.TextField()
    experience = models.TextField(blank=True, null=True)
    skills = models.TextField()
    achievements = models.TextField(blank=True, null=True)

    # New field for AI-generated resume
    generated_text = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.user.username}"

