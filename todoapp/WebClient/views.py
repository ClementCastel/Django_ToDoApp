from django.shortcuts import render

# Create your views here.

def login (request):
	return render(request, 'webclient/login.html', {})

def tasks (request):
	return render(request, 'webclient/add.html', {})

def static (request, file):
	print(file)
	return render(request, 'webclient/'+file, {}, content_type="text/css")