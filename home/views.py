from django.shortcuts import redirect, render
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
                send_mail(subject, message, 'django.heimgartner@gmail.com', ['django.heimgartner@gmail.com'])
            except BadHeaderError:
                return HttpResponse('invalid header found.')
            return redirect('home:index')

    form = ContactForm

    context = {
        'projects': projects,
        'videos': videos,
        'form': form,
    }

    return render(request, 'home/index.html', context)
