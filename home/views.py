from django.shortcuts import redirect, render
from home.models import PageContent
from projects.models import ProjectItem
from videos.models import VideoItem

from postoffice.forms import ContactForm
from django.conf import settings
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
            try:
                subject = 'Hey Djang! contact form'
                body = {
                    'name': form.cleaned_data['name'],
                    'email': form.cleaned_data['email'],
                    'message': form.cleaned_data['message'],
                }
                message = '\n'.join(body.values())
                receiver = settings.EMAIL_HOST_USER
                send_mail(subject, message, receiver, [receiver])
            except BadHeaderError:
                return HttpResponse('invalid header found.')
            return redirect('home:index')
    else:
        form = ContactForm()

    context = {
        'content': content,
        'projects': projects,
        'videos': videos,
        'contact_form': form,
    }
    return render(request, 'home/index.html', context)
