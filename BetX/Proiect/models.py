from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Pronostic(models.Model):
	pronostic_text = models.CharField(max_length = 200)
	publication_date = models.DateTimeField('date published')
	def __str__(self):
		return self.pronostic_text
	def was_published_recently(self):
		return self.publication_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	pronostic = models.ForeignKey(Pronostic, on_delete = models.CASCADE)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)
	def __str__(self):
		return self.choice_text
