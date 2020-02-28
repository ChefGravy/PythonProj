from django.conf.urls import url
#you can use . vs basic_app
from basic_app import views

#TEMPLATE TAGGING
#this will allow template tagging
app_name = 'basic_app'

urlpatterns = [
#after landing on urls.py from project, it will get directed here and below urls will start to work
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
