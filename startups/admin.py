from django.contrib import admin
from .models import Startup

@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'founded_year', 'created_at')
    search_fields = ('name',)
