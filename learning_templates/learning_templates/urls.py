"""learning_templates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from basic_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #the ^$ basically means this is what they see as soon as they hit the page
    url(r'^$', views.index, name = 'index'),
    #they would need to type basic_app in order to go there
    #they would go to basic app and because there is a slash after, it would go to that urls
    url(r'^basic_app/', include('basic_app.urls'))
]
