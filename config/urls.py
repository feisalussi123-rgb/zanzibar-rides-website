from django.contrib import admin
from django.urls import path

from bookings.views import booking_api, contact_api, homepage

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homepage, name="homepage"),
    path("api/bookings/", booking_api, name="booking-api"),
    path("api/messages/", contact_api, name="contact-api"),
]
