from django.db import models

import uuid

# Create your models here.

class User (models.Model):
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	email = models.EmailField(max_length=100)
	password = models.CharField(max_length=130)
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	registerDate = models.DateTimeField(auto_now=True)

	def __str__ (self):
		return str(self.uuid)

class Task (models.Model):
	userUUID = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=300)
	finishDate = models.DateTimeField('deadline date')
	finished = models.BooleanField(default=False)

	def __str__ (self):
		return self.title