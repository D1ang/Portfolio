from django.shortcuts import render
from projects.models import ProjectItem
from videos.models import VideoItem


def index(request):
    """
    A view that displays the index page.
    """
    projects = ProjectItem.objects.all()
    videos = VideoItem.objects.all()

    context = {
        'projects': projects,
        'videos': videos,
    }

    return render(request, 'home/index.html', context)
