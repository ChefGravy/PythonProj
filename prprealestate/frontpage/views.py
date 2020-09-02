
#allows us to send email with our setting
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
# from django.db import models
from frontpage import models
from frontpage.models import ContactForm
from .forms import ContactForm
from django.views.generic import TemplateView


# Create your views here.
# class MembershipView(TemplateView):
#     model = models.MembershipForm
#     template_name='frontpage/index.html'

def contact(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                category = form.cleaned_data['category']
                subject = form.cleaned_data['subject']
                body = form.cleaned_data['body']
                form.save()
                #send_mail(subject, message, from_email, fail_silently=True)
                subject_email = 'PRP Real Estate'
                message_email = 'Welcome and thank you for your e-mail! I will be in touch soon.'
                from_email = settings.EMAIL_HOST_USER
                #this e-mail is for owner with all the details
                send_mail(subject, 'Name: ' + name + '\nEmail of sender: ' + email + '\nCategory: ' + category + '\nSubject: ' + subject + '\nBody: '+ body, email, [from_email], fail_silently=True)
                #this e-mail is for user
                send_mail(subject_email, message_email, 'ruslan@uw.edu',[email], fail_silently=True)

        form = ContactForm()
        return render(request, 'frontpage/contactform.html', {'form':form})

class AboutView(TemplateView):
    template_name = 'frontpage/about.html'

    class Meta:
        verbose_name_plural = 'About'

class BlogView(TemplateView):
    template_name = 'frontpage/blog.html'

    class Meta:
        verbose_name_plural = 'Blog'

class DataView(TemplateView):
    template_name = 'frontpage/data.html'

    class Meta:
        verbose_name_plural = 'Data'
