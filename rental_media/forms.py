from django import forms

from .models import RentalMedia


class RentalMediaForm(forms.ModelForm):
    class Meta:
        model = RentalMedia
        fields = ("title", "media_type", "file")
        widgets = {"file": forms.ClearableFileInput(attrs={"accept": "image/*,video/*"})}

    def clean_file(self):
        uploaded_file = self.cleaned_data["file"]
        allowed_types = {"image/jpeg", "image/png", "image/webp", "image/gif", "video/mp4", "video/webm", "video/quicktime"}
        if uploaded_file.content_type not in allowed_types:
            raise forms.ValidationError("Upload JPG, PNG, WEBP, GIF, MP4, WEBM or MOV only.")
        if uploaded_file.size > 50 * 1024 * 1024:
            raise forms.ValidationError("The maximum file size is 50 MB.")
        return uploaded_file
