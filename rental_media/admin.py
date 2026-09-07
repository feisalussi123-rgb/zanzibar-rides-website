from django.contrib import admin
from django.utils.html import format_html

from .models import RentalMedia


@admin.register(RentalMedia)
class RentalMediaAdmin(admin.ModelAdmin):
    list_display = (
        "preview",
        "title",
        "media_type",
        "is_hero",
        "uploaded_at",
    )

    list_filter = (
        "media_type",
        "is_hero",
        "uploaded_at",
    )

    search_fields = (
        "title",
    )

    ordering = ("-uploaded_at",)

    readonly_fields = (
        "preview_large",
        "uploaded_at",
    )

    fieldsets = (
        (
            "Media Information",
            {
                "fields": (
                    "title",
                    "media_type",
                    "file",
                    "is_hero",
                )
            },
        ),
        (
            "Preview",
            {
                "fields": (
                    "preview_large",
                    "uploaded_at",
                )
            },
        ),
    )

    def preview(self, obj):
        if obj.file and obj.media_type == "image":
            return format_html(
                '<img src="{}" width="80" height="55" '
                'style="object-fit:cover;border-radius:8px;" />',
                obj.file.url,
            )
        return "—"

    preview.short_description = "Preview"

    def preview_large(self, obj):
        if obj.file and obj.media_type == "image":
            return format_html(
                '<img src="{}" width="300" '
                'style="max-height:220px;object-fit:cover;border-radius:12px;" />',
                obj.file.url,
            )
        return "No image preview"

    preview_large.short_description = "Image Preview"