"""rprealestate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

app_name = 'frontpage'

from django.contrib import admin
from django.urls import path, include, reverse
from frontpage import views
from frontpage.views import AboutView



urlpatterns = [
    path('contactform/', views.contact, name = 'contactform'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('data/', views.DataView.as_view(), name ='data'),
]