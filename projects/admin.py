from django.contrib import admin
from .models import ProjectItem


class ProjectItemAdmin(admin.ModelAdmin):
    ordering = ['title']
    list_display = (
        'title',
    )

admin.site.register(ProjectItem, ProjectItemAdmin)
