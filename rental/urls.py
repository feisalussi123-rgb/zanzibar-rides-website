from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from bookings.views import booking_api, contact_api, homepage

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homepage, name="homepage"),
    path("api/bookings/", booking_api, name="booking-api"),
    path("api/messages/", contact_api, name="contact-api"),
    path("media-upload/", include("rental_media.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
