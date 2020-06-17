from django.views.generic import TemplateView
from django.urls import reverse
from django.http import HttpResponseRedirect

#home page is connected to index here
#after this we will update urls.py
# Create your views here.

class TestPage(TemplateView):
    template_name='test.html'

class ThanksPage(TemplateView):
    template_name='thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)