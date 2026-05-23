from django.contrib import admin
from .models import WaitlistEntry

@admin.register(WaitlistEntry)
class WaitlistAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role', 'skill', 'joined_at')
    list_filter = ('role', 'skill')