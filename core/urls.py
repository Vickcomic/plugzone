from django.contrib import admin
from django.urls import path
from services.views import landing, waitlist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),
    path('waitlist/', waitlist, name='waitlist'),
]