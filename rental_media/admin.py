from django.contrib import admin

from .models import RentalMedia


@admin.register(RentalMedia)
class RentalMediaAdmin(admin.ModelAdmin):
    list_display = ("title", "media_type", "uploaded_at", "file")
    list_filter = ("media_type", "uploaded_at")
    search_fields = ("title",)
