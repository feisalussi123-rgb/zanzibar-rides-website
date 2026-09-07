from django.db import models


class Vehicle(models.Model):
    CATEGORY_CHOICES = [
        ("car", "Car"),
        ("scooter", "Scooter"),
    ]

    name = models.CharField(max_length=120)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price_usd = models.DecimalField(max_digits=10, decimal_places=2)
    price_tzs = models.DecimalField(max_digits=12, decimal_places=2)
    seats = models.CharField(max_length=30)
    transmission = models.CharField(max_length=30, default="Automatic")
    image = models.ImageField(upload_to="vehicles/", blank=True, null=True)
    available = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


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