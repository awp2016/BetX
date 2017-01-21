from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.encoding import smart_unicode

# Create your models here.
class Match(models.Model):
	user = models.ForeignKey(User)
	subject = models.CharField(max_length=200)
	def __str__(self):
		return self.subject


class Pronostic(models.Model):
	user = models.ForeignKey(User)
	match = models.ForeignKey(Match, on_delete = models.CASCADE)
	pronostic_text = models.CharField(max_length = 200)
	publication_date = models.DateTimeField('date published')
	def __str__(self):
		return self.pronostic_text
	def was_published_recently(self):
		return self.publication_date >= timezone.now() - datetime.timedelta(days=1)


class Vote(models.Model):
	pronostic = models.ForeignKey(Pronostic, on_delete = models.CASCADE)
	user = models.ForeignKey(User)
	vote_value = models.CharField(max_length = 200)
	def __str__(self):
		return self.vote_text


class Commnent(models.Model):
	pronostic = models.ForeignKey(Pronostic, on_delete = models.CASCADE)
	author = models.ForeignKey(User)
	comment_text = models.CharField(max_length = 200)
	publication_date = models.DateTimeField('date published')
	

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
    email = models.EmailField()
    birthday = models.DateField(null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default=MALE)
    user = models.OneToOneField(User, primary_key=True, related_name='profile')
