from django.db import models
from django.db.models.fields import CharField, EmailField

# Create your models here.

class User(models.Model):
    name = CharField(max_length=50)
    email = EmailField(max_length=100)
    password = CharField(max_length=100)