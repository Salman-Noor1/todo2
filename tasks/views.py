from turtle import title
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Task

# Create your views here.
def home(request):
    # retrieves all tasks from the database
    tasks = Task.objects.all()
    
    if request.method =="POST":
        data = request.POST
        task = data.get("task")
        # add task into the database
        Task.objects.create(title=task)

    context = {
        "tasks": tasks
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

