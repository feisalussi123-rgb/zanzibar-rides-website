from config.settings import *

ROOT_URLCONF = "rental.urls"
TEMPLATES[0]["DIRS"] = [BASE_DIR / "templates"]
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
