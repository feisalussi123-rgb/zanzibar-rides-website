from config.settings import *

import os
import dj_database_url

ROOT_URLCONF = "rental.urls"

TEMPLATES[0]["DIRS"] = [BASE_DIR / "templates"]

STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

STORAGES = {
 "default": {
 "BACKEND": "django.core.files.storage.FileSystemStorage",
 },
 "staticfiles": {
 "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
 },
}

if os.environ.get("DATABASE_URL"):
 DATABASES["default"] = dj_database_url.config(
 default=os.environ.get("DATABASE_URL"),
 conn_max_age=600,
 ssl_require=True,
 )
