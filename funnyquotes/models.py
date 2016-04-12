from django.db import models

# Create your models here.
class FamousQuote(models.Model):
	quote = models.CharField(max_length=200)
	author = models.CharField(max_length=50)

	def __unicode__(self):
		return self.quote

class InfamousQuote(models.Model):
	add = models.CharField(max_length=200)

	def __unicode__(self):
		return self.add