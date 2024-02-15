from django.db import models
from datetime import datetime

# Create your models here.
CONTENT_FIELD = (
    ("SELECTED", 'Selected'),
    ("UNSELECTED", 'UnSelected')
)

class HotelData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(default=None)
    address = models.TextField(default=None)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=datetime.now)

class ContentData(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200,default=None)
    content = models.TextField(default=None)
    status = models.CharField(max_length=100,choices=CONTENT_FIELD,default="UNSELECTED")
    created_at = models.DateTimeField(default=datetime.now)