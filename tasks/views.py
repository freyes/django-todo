# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Task
from forms import TaskForm

def get(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = TaskForm()

    tasks = Task.objects.all()
    uncompleteCount = Task.objects.filter(completed=False).count()

    return render(request, 'tasks/index.html', {
        'name': 'World', 
        'form': form,
        'tasks': tasks,
        'uncompleteCount': uncompleteCount,
    })