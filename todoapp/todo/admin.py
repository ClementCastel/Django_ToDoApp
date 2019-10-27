from django.contrib import admin
from .models import List, Task

# Register your models here.

#admin.site.register(List)
#admin.site.register(Task)
admin.site.site_header = "ToDo APP"


class TaskInLine(admin.TabularInline):
	model = Task
	extra = 1

class ListAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['title']}), ]
	inlines = [TaskInLine]

admin.site.register(List, ListAdmin)