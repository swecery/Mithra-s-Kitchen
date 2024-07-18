from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reservation for {self.user.username} on {self.reservation_date} at {self.reservation_time}"
