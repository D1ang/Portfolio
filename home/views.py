from django.shortcuts import render
from projects.models import ProjectItem
from videos.models import VideoItem

from django.core.mail import EmailMessage
from home.forms import ContactForm


def index(request):
    """
    Load the homepage if there is no POST request.
    If POST load the data & send an email.
    """
    projects = ProjectItem.objects.all()
    videos = VideoItem.objects.all()

    form = ContactForm

    context = {
        'projects': projects,
        'videos': videos,
        'form': form,
    }

    return render(request, 'home/index.html', context)
