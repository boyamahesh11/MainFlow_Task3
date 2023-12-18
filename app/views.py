# tasks/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from app.models import *
from app.forms import *

@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def task_new(request):
    if request.method == "POST":
        content = request.POST.get('content')
        Task.objects.create(content=content)
        return redirect('task_list')
    return render(request, 'tasks/task_form.html')

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.content = request.POST.get('content')
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'task': task})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')
