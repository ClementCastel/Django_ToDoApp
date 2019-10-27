from django.shortcuts import render

from .models import Task, List
# Create your views here.

def index (request):

	tasks = Task.objects.filter(finished=False).order_by('finishDate')
	context = {'tasks': tasks, 'title': 'Index'}

	return render(request, 'todo/index.html', context)

def finished (request):

	tasks = Task.objects.filter(finished=True).order_by('-finishDate')
	context = {'tasks': tasks, 'title': 'Finished'}

	return render(request, 'todo/index.html', context)
