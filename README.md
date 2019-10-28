# Django_ToDoApp
To Do app built in Django

---
## API:
### tasks:
GET
- /<uuid>/all/ : all tasks
- /<uuid>/unfinished/ : unfinished tasks
- /<uuid>/next/<int>/ : n(int) last tasks
- /<uuid>/past/ : overdue tasks
- /<uuid>/future : upcoming tasks