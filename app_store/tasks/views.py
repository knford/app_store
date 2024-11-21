from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Item

def home(request):
    tasks = Task.objects.all().order_by('due_date', 'due_time')

    return render(request, 'index.html', {
        'tasks': tasks,
    })


def completed(request):
    completed_tasks = Task.objects.filter(completed=True).order_by('due_date', 'due_time')
    return render(request, 'completed.html', {
        'tasks': completed_tasks,
    })

def remaining(request):
    remaining_tasks = Task.objects.filter(completed=False).order_by('due_date', 'due_time')
    return render(request, 'remaining.html', {
        'tasks': remaining_tasks,
    })


def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        due_time = request.POST.get('due_time')
        completed = False

        if title != "" and due_date != "" and due_time != "":
            task = Task(
                title = title,
                description = description,
                due_date = due_date,
                due_time = due_time,
                completed = completed
            )
            task.save()
            return redirect('home')
    else:
        return render(request, 'add_task.html')
    return render(request, 'add_task.html')

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    # Store the previous URL (or fallback to '/')
    referer = request.META.get('HTTP_REFERER', '/')
    request.session['previous_url'] = referer if referer.startswith(request.build_absolute_uri('/')) else '/'

    return render(request, 'delete.html', {'task': task})

def go_back_view(request):
    # Safely redirect to the stored URL or fallback
    return redirect(request.session.get('previous_url', '/'))

def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'task_detail.html', {'task': task})

def item_detail(request, task_id):
    # Fetch the task using the provided ID
    task = get_object_or_404(Task, pk=task_id)
    # Fetch all items related to this task
    items = Item.objects.filter(task=task)
    return render(request, 'item_detail.html', {'task': task, 'items': items})

def toggle_home(request, task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.completed = not task.completed
        task.save()
        return redirect('index')

def toggle_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.completed = not task.completed
        task.save()
        return redirect('completed')

def toggle_remaining(request, task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.completed = not task.completed
        task.save()
        return redirect('remaining')

def remove_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.delete()
        return redirect('home')