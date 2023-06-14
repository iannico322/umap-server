from django.db import models

# You can create your models here.


class Event(models.Model):
    eventID = models.AutoField(primary_key=True)
    locationID = models.IntegerField()
    title = models.CharField(max_length=255)
    time = models.CharField(max_length=100)
    date = models.DateField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
   
    def __str__(self) -> str:
        return self.locationID
