
# Django_ToDoApp
To Do app built in Django

## API:
### tasks:
GET
- /**\<uuid>**/all/ : all tasks
- /**\<uuid>**/unfinished/ : unfinished tasks
- /**\<uuid>**/finished/ : finished tasks
- /**\<uuid>**/next/**\<int>**/ : n(int) last tasks
- /**\<uuid>**/past/ : overdue tasks
- /**\<uuid>**/future : upcoming tasks
 
POST
- /users/register/ <i>(POST: firstname/lastname/email/password)</i> : add user to DB
- /users/login/ <i>(POST: email/password)</i> : get the UUID of a user
- /users/delete/ <i>(POST: email/password)</i> : remove user from DB