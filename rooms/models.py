from django.db import models

# Attribute fields and data types for Room talble in the database

class Room(models.Model):
    roomID = models.AutoField(primary_key=True)
    roomType = models.CharField(max_length=100)
    roomName = models.CharField(max_length=100)
    buildingNumber = models.IntegerField()
    blockNumber = models.IntegerField()
    floorNumber = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.roomName
