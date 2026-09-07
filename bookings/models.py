from django.db import models


class Booking(models.Model):
    VEHICLE_CHOICES = [("car", "Car"), ("scooter", "Scooter")]

    vehicle = models.CharField(max_length=20, choices=VEHICLE_CHOICES)
    pickup_location = models.CharField(max_length=80)
    pickup_date = models.DateField()
    return_date = models.DateField()
    pickup_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
