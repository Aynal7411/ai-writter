from django.shortcuts import render
from .models import Project, Skill
# Create your views here.
def home_page(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    return render(request, 'home.html', {
        'projects': projects,
        'skills': skills
    })
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data (example: send email)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f"New Contact Message from {name}",
                message,
                email,
                [settings.DEFAULT_FROM_EMAIL],  # Or your own email
                fail_silently=False,
            )
            messages.success(request, "Thanks for reaching out!")
            form = ContactForm()  # Clear the form
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

  