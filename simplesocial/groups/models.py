from django.db import models
#allows spaces in addressses
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
# Create your models here.

#links and markdown tags
import misaka

#get the user model that's currently used. call stuff off the users current session
from django.contrib.auth import get_user_model
#call off the user session
User = get_user_model()
from django import template
#using custom template tag in future
register = template.Library()

class Group(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False,default='',blank=True)
    members = models.ManyToManyField(User,through='GroupMember')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        #slug will become the name once spaces ar removed
        self.slug = slugify(self.name)

        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})

    class Meta:
        ordering=['name']

class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name="memberships", on_delete = models.CASCADE)
    #the User above is going to be part of some user groups
    user = models.ForeignKey(User,related_name="user_groups", on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("group","user")
