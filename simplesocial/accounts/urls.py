from django.conf.urls import url
#django introduced a login and logout view
# we want to make sure we don't confuse this with from . import views
from django.contrib.auth import views as auth_views
#dot means from your own views
from . import views

#need this for app views vs project views
app_name = 'accounts'

urlpatterns=[
#loginurl
    url(r'login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'signup/$', views.SignUp.as_view(), name='signup'),

]
