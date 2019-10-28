from django.db import models

# Create your models here.

class Task (models.Model):
	#listP = models.ForeignKey(List, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	finishDate = models.DateTimeField('deadline date')
	finished = models.BooleanField(default=False)

	def __str__ (self):
		return self.title