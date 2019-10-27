from django.db import models

# Create your models here.

class List (models.Model):
	title = models.CharField(max_length=200)

	def __str__ (self):
		return self.title

class Task (models.Model):
	listP = models.ForeignKey(List, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	finishDate = models.DateTimeField('deadline date')

	def __str__ (self):
		return self.title