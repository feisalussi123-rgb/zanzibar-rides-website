
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from bookings import views


urlpatterns = [
    # =========================
    # MAIN PAGES
    # =========================

    path("admin/", admin.site.urls),

    path("", views.homepage, name="home"),

    path(
        "fleet/",
        views.fleet_page,
        name="fleet",
    ),

    path(
        "how-it-works/",
        views.how_it_works_page,
        name="how_it_works",
    ),

    path(
        "destinations/",
        views.destinations_page,
        name="destinations",
    ),

    path(
        "about/",
        views.about_page,
        name="about",
    ),

    path(
        "contact/",
        views.contact_page,
        name="contact",
    ),

    # =========================
    # API
    # =========================

    path(
        "api/booking/",
        views.booking_api,
        name="booking_api",
    ),

    path(
        "api/contact/",
        views.contact_api,
        name="contact_api",
    ),
]


# =========================
# MEDIA FILES
# =========================

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
