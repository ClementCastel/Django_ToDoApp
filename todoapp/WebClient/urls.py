from django.urls import path

from . import views

app_name = "webclient"
urlpatterns = [
	path('login', views.login, name='Login'),
	path('tasks', views.tasks, name='Tasks'),
	path('static/<file>', views.static, name="Load css")
]