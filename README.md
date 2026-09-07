# Best Ride Zanzibar

Django backend for the Best Ride car and scooter rental website. The project uses
`rental` as its Django project package, `templates/` for HTML, `static/` for CSS
and JavaScript, and `rental_media` for image/video uploads.

## Run locally

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
python manage.py makemigrations bookings rental_media
py manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ and use `/admin/` to review booking and contact submissions.
Open http://127.0.0.1:8000/media-upload/ to upload rental photos and videos.

Uploaded files are stored in `media/uploads/` during development. Configure
`MEDIA_ROOT`, `MEDIA_URL`, and a production object-storage service before deployment.
