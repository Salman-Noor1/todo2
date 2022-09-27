from turtle import title
from django.http import HttpResponse
from django.shortcuts import render,redirect

from tasks.forms import TaskForm
from .models import Task

# Create your views here.
def home(request):
    # retrieves all tasks from the database
    tasks = Task.objects.all()
    form = TaskForm()


    if request.method =="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  

    context = {
        "tasks": tasks,
        "form":form
    }
    return render(request, "base.html", context)

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()

    return redirect("home")


def done_task(request, id):
    task = Task.objects.get(id=id)
    task.done=True
    task.save()

    return redirect("home")

