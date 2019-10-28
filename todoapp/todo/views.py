from django.shortcuts import render
from django.http import HttpResponse

from .models import User, Task
# Create your views here.

def getAllUsers (request):
	users = User.objects.all()
	context = {'users': users}
	print('USERS : ')
	print(context)
	response = HttpResponse()
	response.write("DEBUG : OK")
	return response


def all (request, uuid):
	tasks = Task.objects.order_by('finishDate')
	context = {'tasks': tasks, 'title': 'Index'}

	return render(request, 'todo/index.html', context)
