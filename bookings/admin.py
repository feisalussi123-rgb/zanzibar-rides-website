from django.contrib import admin

from .models import Booking, ContactMessage


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "pickup_location", "pickup_date", "return_date", "created_at")
    list_filter = ("vehicle", "pickup_location")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at")
    search_fields = ("name", "email", "phone")
