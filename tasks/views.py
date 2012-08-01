# Create your views here.
from django.shortcuts import redirect, render
from django.views.generic.base import View
from models import Task
from forms import TaskForm


class TaskIndexView(View):
    template_name = "tasks/index.html"

    def get(self, request, form=None):
        if form is None:
            form = TaskForm()

        tasks = Task.objects.all()
        uncompleteCount = Task.objects.filter(completed=False).count()

        return render(request, 'tasks/index.html', {
            'form': form,
            'tasks': tasks,
            'uncompleteCount': uncompleteCount,
        })

    def post(self, request):

        form = TaskForm(data=request.POST)
        if not form.is_valid():
            return self.get(request, form)

        form.save()
        return redirect('index')
