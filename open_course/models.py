from __future__ import unicode_literals

from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# for storing code later use
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Teacher(models.Model):
	name = models.TextField(max_length = 40)
	email = models.EmailField()
	account = models.TextField(max_length = 40)
	note = models.TextField(blank = True)

	def __unicode__(self):
		return self.name

class Assistant(models.Model):
	name = models.TextField(max_length = 40)
	email = models.EmailField()
	account = models.TextField(max_length = 40)
	note = models.TextField(blank = True)

	def __unicode__(self):
		return self.name

class Supporter(models.Model):
	name = models.TextField(max_length=40)
	email = models.EmailField()

	def __unicode__(self):
		return self.name

class Classroom(models.Model):
	owner = models.ForeignKey('auth.User', related_name='classrooms', on_delete=models.CASCADE)

	created = models.DateTimeField(auto_now_add=True)
	school = models.CharField(max_length=10)
	subject = models.CharField(max_length= 20)
	subject_code = models.CharField(max_length = 20)
	class_name = models.TextField(blank = False)
	class_subject = models.TextField(blank = False)
	estimated_students = models.PositiveIntegerField()
	start_date = models.DateTimeField()
	finish_date = models.DateTimeField()
	examination_date = models.DateTimeField()
	teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
	assistant = models.ForeignKey(Assistant, on_delete = models.CASCADE)
	change_note = models.TextField(blank = True)
	supporter = models.ForeignKey(Supporter, on_delete = models.CASCADE)

	class Meta:
		ordering = ('created',)

	def __unicode__(self):
		return self.subject_code
