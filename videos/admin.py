from django.contrib import admin
from .models import VideoItem


@admin.register(VideoItem)
class VideoItemAdmin(admin.ModelAdmin):
    ordering = ['title']
    list_display = (
        'title',
    )
