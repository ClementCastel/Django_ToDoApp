from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import json

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
	tasks = Task.objects.filter(userUUID=uuid).order_by('finishDate').values('title', 'finishDate')

	data = []
	for t in tasks:
		data.append({'title': t['title'], 'finishDate': datetime.timestamp(t['finishDate'])})

	return HttpResponse(json.dumps(data), content_type='application/json')


def unfinished (request, uuid):
	tasks = Task.objects.filter(userUUID=uuid).filter(finished=False).order_by('finishDate').values('title', 'finishDate')

	data = []
	for t in tasks:
		data.append({'title': t['title'], 'finishDate': datetime.timestamp(t['finishDate'])})

	return HttpResponse(json.dumps(data), content_type='application/json')


def finished (request, uuid):
	tasks = Task.objects.filter(userUUID=uuid).filter(finished=True).order_by('finishDate').values('title', 'finishDate')

	data = []
	for t in tasks:
		data.append({'title': t['title'], 'finishDate': datetime.timestamp(t['finishDate'])})

	return HttpResponse(json.dumps(data), content_type='application/json')


def next (request, uuid, next):
	tasks = Task.objects.filter(userUUID=uuid).filter(finished=False).order_by('finishDate').values('title', 'finishDate')[:next]

	data = []
	for t in tasks:
		data.append({'title': t['title'], 'finishDate': datetime.timestamp(t['finishDate'])})

	return HttpResponse(json.dumps(data), content_type='application/json')


def past (request, uuid):
	tasks = Task.objects.filter(userUUID=uuid).filter(finished=False).filter(finishDate__lt=datetime.now()).order_by('finishDate').values('title', 'finishDate')

	data = []
	for t in tasks:
		data.append({'title': t['title'], 'finishDate': datetime.timestamp(t['finishDate'])})

	return HttpResponse(json.dumps(data), content_type='application/json')


def future (request, uuid):
	tasks = Task.objects.filter(userUUID=uuid).filter(finished=False).filter(finishDate__gt=datetime.now()).order_by('finishDate').values('title', 'finishDate')

	data = []
	for t in tasks:
		data.append({'title': t['title'], 'finishDate': datetime.timestamp(t['finishDate'])})

	return HttpResponse(json.dumps(data), content_type='application/json')