from django.shortcuts import redirect, render
from home.models import PageContent
from projects.models import ProjectItem
from videos.models import VideoItem

from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def index(request):
    """
    Load the homepage if there is no POST request.
    If POST load the data & send an email.
    """
    content = PageContent.objects.first()
    projects = ProjectItem.objects.all()
    videos = VideoItem.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = 'Hey Djang! contact form'
            body = {
                'contact_name': form.cleaned_data['contact_name'],
                'contact_email': form.cleaned_data['contact_email'],
                'message': form.cleaned_data['message'],
            }
            message = '\n'.join(body.values())

            try:
                send_mail(subject, message, 'info@tanooki.nl', ['info@tanooki.nl'])
            except BadHeaderError:
                return HttpResponse('invalid header found.')
            return redirect('home:index')

    form = ContactForm

    context = {
        'content': content,
        'projects': projects,
        'videos': videos,
        'form': form,
    }

    return render(request, 'home/index.html', context)
