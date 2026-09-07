from django.contrib import admin
from .models import Booking, ContactMessage, Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price_usd",
        "price_tzs",
        "seats",
        "transmission",
        "available",
    )

    list_filter = (
        "category",
        "available",
        "transmission",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = ("name",)

    list_editable = (
        "price_usd",
        "price_tzs",
        "available",
    )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "vehicle",
        "pickup_location",
        "pickup_date",
        "return_date",
        "pickup_time",
        "created_at",
    )

    list_filter = (
        "vehicle",
        "pickup_location",
        "pickup_date",
        "return_date",
    )

    search_fields = (
        "pickup_location",
        "vehicle",
    )

    ordering = ("-created_at",)
    readonly_fields = ("created_at",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "message",
    )

    list_filter = ("created_at",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)