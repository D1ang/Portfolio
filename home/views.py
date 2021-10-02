from django.shortcuts import render
from projects.models import ProjectItem


def index(request):
    """
    A view that displays the index page.
    """
    projects = ProjectItem.objects.all()

    context = {'projects': projects}

    return render(request, 'home/index.html', context)
