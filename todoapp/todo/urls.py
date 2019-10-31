from django.urls import path

from . import views

app_name = "todo"
urlpatterns = [
	#DEBUG - - - -
	path('getAllUsers/', views.getAllUsers, name='DEBUG-getAllUsers'),
	# PROD - - - -	
	# TASK MODEL
	path('<uuid:uuid>/all/', views.all, name='all'),
	path('<uuid:uuid>/unfinished/', views.unfinished, name='unfinished'),
	path('<uuid:uuid>/finished/', views.finished, name='finished'),
	path('<uuid:uuid>/next/<int:next>/', views.next, name='next'),
	path('<uuid:uuid>/past/', views.past, name='past'),
	path('<uuid:uuid>/future/', views.future, name='future'),
	# FINISH / UNFINISH
	path('<uuid:uuid>/finish/<uuid:task>/', views.finish, name='finish'),
	path('<uuid:uuid>/unfinish/<uuid:task>/', views.unfinish, name='unfinish'),
	path('<uuid:uuid>/add/', views.add, name='unfinish'),
	# USER MODEL
	path('users/delete/', views.userDelete, name='delete user'),
	path('users/register/', views.userRegister, name='register user'),
	path('users/login/', views.userLogin, name='user login')
]