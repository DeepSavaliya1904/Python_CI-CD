from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    user_id=models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False) 
    name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    