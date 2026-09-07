from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import RentalMediaForm
from .models import RentalMedia


def upload_media(request):
    if request.method == "POST":
        form = RentalMediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Media uploaded successfully.")
            return redirect("media-upload")
    else:
        form = RentalMediaForm()
    return render(request, "media_upload.html", {"form": form, "media_items": RentalMedia.objects.all()})
