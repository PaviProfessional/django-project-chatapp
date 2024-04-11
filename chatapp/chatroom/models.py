from django.db import models
from datetime import datetime
# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=100)
class Message(models.Model):
    value=models.CharField(max_length=100000)              # message
    date=models.TimeField(default=datetime.now,blank="True")
    user=models.CharField(max_length=100)
    room=models.CharField(max_length=100)     #it will give the room id for us


