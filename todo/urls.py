from django.urls import path 
from . import views

app_name = 'todo'

urlpatterns = [
    path('' ,views.home , name='home'),
    path('detail/<int:id>' ,views.task_detail , name='detail'),
    path('add/' ,views.add_task , name='add_task'),
    path('complete/<int:id>/', views.complete_task, name='complete_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('login/' , views.logedin, name = 'login') ,
    path('logout/' , views.logedout, name = 'logout') ,
    path('register/' , views.Registered , name = 'register'),
    path('DELETE/' , views.Delete_account , name = 'Delete_account'),
    
    

]
