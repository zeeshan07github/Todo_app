from django.shortcuts import render ,redirect
from .models import *

from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    # Filter tasks based on the currently logged-in user
    tasks = Task.objects.filter(user=request.user)

    # Separate completed and incomplete tasks
    completed_tasks = tasks.filter(completed=True)
    incomplete_tasks = tasks.filter(completed=False)

    context = {
        'completed_tasks': completed_tasks,
        'incomplete_tasks': incomplete_tasks,
    }

    return render(request, 'todo/home.html', context)


def task_detail(request , id):
    task_todo = Task.objects.get(id = id)
    context = {
        'task_todo' : task_todo
    }
    return render(request , 'todo/detail.html' , context) 


@login_required
def add_task(request):
    if request.method == 'POST':
        form = add_form(request.POST)
        if form.is_valid():
            # Set the user field to the currently logged-in user
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todo:home')
    else:
        form = add_form()
    return render(request, 'todo/addtodo.html', {'form': form})


@login_required
def complete_task(request, id):
    task = Task.objects.get( id = id)
    task.completed = True
    task.save()
    return redirect('todo:home')

@login_required
def delete_task(request, id):
    task = Task.objects.get(id = id)
    if request.method == 'POST':
        task.delete()
        return redirect('todo:home')
    return render(request , 'todo/tdelete.html' , {'task':task})

def logedin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request , request.POST)
        if form.is_valid():
            user = form.get_user()
            login (request, user)
            return redirect('todo:home')
    else:
        form = AuthenticationForm()
    return render(request , 'todo/login.html' , {"form" : form})

def Registered(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo:login")
    else:
        form = UserCreationForm()
    return render(request , 'todo/register.html' , {"form" : form})


def logedout(request):
    logout(request)
    return redirect("todo:login")

def Delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request , "Your account has been deleted!")
        return redirect('todo:login')
    return render(request , 'todo/udelete.html' )