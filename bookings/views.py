import json
from datetime import date

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Booking, ContactMessage
from .fleet import FLEET
from rental_media.models import RentalMedia


def homepage(request):
    return render(request, "index.html", {"fleet": FLEET, "media_items": RentalMedia.objects.all()[:8]})


def parse_json(request):
    try:
        return json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return None


@csrf_exempt
@require_http_methods(["POST"])
def booking_api(request):
    data = parse_json(request)
    required = ("vehicle", "pickup_location", "pickup_date", "return_date", "pickup_time")
    if data is None or any(not data.get(field) for field in required):
        return JsonResponse({"error": "Please complete all booking fields."}, status=400)
    if data["vehicle"] not in {"car", "scooter"}:
        return JsonResponse({"error": "Choose a valid vehicle."}, status=400)
    try:
        pickup_date = date.fromisoformat(data["pickup_date"])
        return_date = date.fromisoformat(data["return_date"])
    except ValueError:
        return JsonResponse({"error": "Enter valid pickup and return dates."}, status=400)
    if return_date < pickup_date:
        return JsonResponse({"error": "Return date must be after pickup date."}, status=400)
    booking = Booking.objects.create(
        vehicle=data["vehicle"],
        pickup_location=data["pickup_location"],
        pickup_date=pickup_date,
        return_date=return_date,
        pickup_time=data["pickup_time"],
    )
    return JsonResponse({"message": f"Booking request #{booking.pk} received. We will confirm shortly."}, status=201)


@csrf_exempt
@require_http_methods(["POST"])
def contact_api(request):
    data = parse_json(request)
    required = ("name", "email", "message")
    if data is None or any(not str(data.get(field, "")).strip() for field in required):
        return JsonResponse({"error": "Please enter your name, email and message."}, status=400)
    message = ContactMessage.objects.create(
        name=str(data["name"]).strip(),
        email=str(data["email"]).strip(),
        phone=str(data.get("phone", "")).strip(),
        message=str(data["message"]).strip(),
    )
    return JsonResponse({"message": f"Thanks, {message.name}. We will reply shortly."}, status=201)
