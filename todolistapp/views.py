from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from .models import Task
from .forms import Taskform
# Create your views here.
# def Todolistview(request):
#     object = Task.objects.all()
#     form = Taskform(request.POST or None)    
#     if form.is_valid():
#         form.save()
#         form = Taskform()
#     context = {
#     "tasks" : object,
#     "form":form,
#     }
#     return render(request,"todolist.html",context)

def Todolistview(request):
    object = Task.objects.all()
    context = {
    "tasks" : object,
    }
    return render(request,"todolist.html",context)

def addtask(request):
    Form = Taskform(request.POST or None)
    if request.method == "POST":
        Form.save()
        Form = Taskform()
        return redirect("home")
    context = {
        "form":Form,
    }
    return render(request,"addtask.html",context)


def taskdelete(request,event):
    TASK = Task.objects.get(id=event)
    TASK.delete()
    return redirect("home") 

def task_edit(request,event):
    OBJECT= Task.objects.get(id=event)
    form = Taskform(request.POST or None,instance=OBJECT)
    if form.is_valid():
        form.save()
        return redirect("home")
    context = {
        "form":form,
    }
    return render(request,"addtask.html",context)