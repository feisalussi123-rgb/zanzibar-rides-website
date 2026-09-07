from django.db import models


class RentalMedia(models.Model):
    MEDIA_TYPES = [("image", "Image"), ("video", "Video")]

    title = models.CharField(max_length=160)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    file = models.FileField(upload_to="uploads/%Y/%m/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return self.title
