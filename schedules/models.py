from django.db import models

# Model for Schedule

class Schedule(models.Model):
    scheduleID = models.AutoField(primary_key=True)
    userID = models.IntegerField()
    roomID = models.IntegerField()
    title = models.CharField(max_length=255)
    time = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
