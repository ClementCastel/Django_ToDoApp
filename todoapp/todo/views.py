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
	tasks = Task.objects.filter(userUUID=uuid).order_by('finishDate')
	context = {'tasks': tasks, 'title': 'Index'}

	return render(request, 'todo/index.html', context)


def unfinished (request, uuid):
	tasks = Task.objects.order_by('finishDate')

	context = {'tasks': tasks}

	return HttpResponse("unfinished")


def finished (request, uuid):
	tasks = Task.objects.order_by('finishDate')

	context = {'tasks': tasks}

	return HttpResponse("finished")


def next (request, uuid, next):
	tasks = Task.objects.order_by('finishDate')

	context = {'tasks': tasks}

	return HttpResponse("next")


def past (request, uuid):
	# datetime.now()
	tasks = Task.objects.order_by('finishDate')

	context = {'tasks': tasks}

	return HttpResponse("past")


def future (request, uuid):
	# datetime.now()
	tasks = Task.objects.order_by('finishDate')

	context = {'tasks': tasks}

	return HttpResponse("future")