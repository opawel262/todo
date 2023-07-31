from django.shortcuts import render, redirect
from .models import Task
# Create your views here.

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    context = {
        'tasks':tasks,
    }
    return render(request, 'home.html', context)

def addTask(request):
    if request.method == 'POST':
        task = request.POST['task']
        Task.objects.create(task=task)
    return redirect('home')