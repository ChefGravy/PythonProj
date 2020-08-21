from django.db import models

# Create your models here.
class MembershipForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    subject = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return self.name
