from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.encoding import smart_unicode

class SignUp(models.Model):
	first_name = models.CharField(max_length=120, null=True, blank=True)
	last_name = models.CharField(max_length=120, null=True, blank=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=True,auto_now=False)

	def __unicode__(self):
		return smart_unicode(self.email)

class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'F'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default=MALE)
    user = models.OneToOneField(User, primary_key=True, related_name='profile')
