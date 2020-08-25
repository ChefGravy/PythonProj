from django.shortcuts import render
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
