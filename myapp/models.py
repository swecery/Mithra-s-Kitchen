from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Reservation by {self.user.username} on {self.date} at {self.time} for {self.guests} guests"