from django.contrib import admin
from .models import ScrapedData

# Register your models here.
admin.site.register(ScrapedData)
class ScrapedDataAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "url", "created_at")
    search_fields = ("title", "url")
    list_filter = ("created_at",)
