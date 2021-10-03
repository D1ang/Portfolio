from django.contrib import admin
from .models import VideoItem


class VideoItemAdmin(admin.ModelAdmin):
    ordering = ['title']
    list_display = (
        'title',
    )

admin.site.register(VideoItem, VideoItemAdmin)
