from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
	title = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		return ('question_detail', [str(self.id)])

class Option(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	question = models.ForeignKey(Question)
	voters = models.ManyToManyField(User)

	def __unicode__(self):
		return self.title