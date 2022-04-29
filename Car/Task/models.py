from django.db import models

class carlist(models.Model):
    CarName=models.CharField(max_length=30)
    Price=models.IntegerField()
    Ratings=models.DecimalField(max_digits=10, decimal_places=2)
    Brand=models.CharField(max_length=30)
    Modelyear=models.IntegerField()
    City=models.CharField(max_length=20, default=0)
    Carcount=models.IntegerField(default=0)
    Show_roomName=models.CharField(max_length=20, default=0)

    def __str__(self):
        return self.CarName

class Show_room(models.Model):
    Name=models.CharField(max_length=25)
    City=models.CharField(max_length=20)
    Carcount=models.IntegerField(default=0)

    def __str__(self):
        return self.Name