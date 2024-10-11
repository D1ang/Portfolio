from django.contrib import admin
from .models import ProjectItem


@admin.register(ProjectItem)
class ProjectItemAdmin(admin.ModelAdmin):
    ordering = ['title']
    list_display = (
        'title',
    )
