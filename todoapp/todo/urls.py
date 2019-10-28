from django.urls import path

from . import views

app_name = "todo"
urlpatterns = [
	#DEBUG - - - -
	path('getAllUsers/', views.getAllUsers, name='DEBUG-getAllUsers'),
	# PROD - - - -	
	path('<uuid:uuid>/all/', views.all, name='all'),
	path('<uuid:uuid>/unfinished/', views.unfinished, name='unfinished'),
	path('<uuid:uuid>/finished/', views.finished, name='finished'),
	path('<uuid:uuid>/next/<int:next>/', views.next, name='next'),
	path('<uuid:uuid>/past/', views.past, name='past'),
	path('<uuid:uuid>/future/', views.future, name='future')
]