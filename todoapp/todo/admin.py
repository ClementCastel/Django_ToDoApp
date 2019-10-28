from django.contrib import admin
from .models import User, Task

# Register your models here.

#admin.site.register(List)
#admin.site.register(Task)
admin.site.site_header = "ToDo APP"


class TaskInLine(admin.TabularInline):
	model = Task
	extra = 1

class UserAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['email']}), (None, {'fields': ['password']}), (None, {'fields': ['firstname']}), (None, {'fields': ['lastname']})]
	inlines = [TaskInLine]

	'''email = models.EmailField(max_length=100)
	password = models.CharField(max_length=130)
	firstName = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)'''

admin.site.register(User, UserAdmin)