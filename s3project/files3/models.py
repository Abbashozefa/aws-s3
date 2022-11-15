from django.db import models

# Create your models here.
class upload(models.Model):
    files=models.FileField(upload_to='media/')
class uploads(models.Model):
    files=models.FileField(upload_to='media/')
