from django.db import models

class Lead(models.Model):
    
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100, unique=True)
    phone_number=models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)
