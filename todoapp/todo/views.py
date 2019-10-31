from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password,check_password

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





@csrf_exempt
def userRegister (request):
	#POST
	if request.method == 'POST':
		if request.POST.get('firstname', None) is not None and request.POST.get('lastname', None) is not None and request.POST.get('email', None) is not None and request.POST.get('password', None) is not None:
			exists = User.objects.filter(email=request.POST['email']).count()
			if exists == 0:
				user = User.create(request.POST['email'], make_password(request.POST['password']), request.POST['firstname'], request.POST['lastname'])
				user.full_clean()
				user.save()
				return HttpResponse("user created", status=201)
			else:
				return HttpResponse('user already exists', status=404)
		return HttpResponse("invalid POST request", status=404)
	else:
		return HttpResponse(status=405)


@csrf_exempt
def userLogin (request):
	#POST
	if request.method == 'POST':
		if request.POST.get('email', None) is not None and request.POST.get('password', None) is not None:
			user = User.objects.filter(email=request.POST['email'])
			if user and user[0] and check_password(password=request.POST['password'], encoded=user[0].password):
				return HttpResponse(user[0].uuid, status=200)
			else:
				return HttpResponse('user not found', status=404)
		elif request.body is not None:
			body_unicode = request.body.decode('utf-8')
			body = json.loads(body_unicode)
			email = body['email']
			password = body['password']
			user = User.objects.filter(email=email)
			print("email : "+str(email))
			if user and user[0] and check_password(password=password, encoded=user[0].password):
				print(user[0].uuid)
				return HttpResponse(""+str(user[0].uuid), status=200)
			else:
				return HttpResponse('user not found', status=404)
		else:
			print(request.body)
			print("email : "+request.POST.get('email', 'none')+" : : "+request.POST.get('password', 'none'))
			return HttpResponse('invalid POST request', status=404)
	elif request.method == 'OPTIONS':
		return HttpResponse(status=200)
	else:
		return HttpResponse(status=405)


@csrf_exempt
def userDelete (request):
	#POST
	if request.method == 'POST':
		print(request.POST)
		if request.POST.get('email', None) is not None and request.POST.get('password', None) is not None:
			user = User.objects.filter(email=request.POST['email'])
			if user and user[0] and check_password(password=request.POST['password'], encoded=user[0].password):
				#delete user
				user[0].delete()
				return HttpResponse('user deleted', status=202)
			else:
				return HttpResponse('user not found', status=404)
		else:
			return HttpResponse('invalid POST request', status=404)
	else:
		return HttpResponse(status=405)