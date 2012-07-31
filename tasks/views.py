# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Task
from forms import TaskForm
from app.views import RestView


class TaskIndexView(RestView):

    def GET(self, request):
        form = TaskForm()
        tasks = Task.objects.all()
        uncompleteCount = Task.objects.filter(completed=False).count()

        return render(request, 'tasks/index.html', {
            'form': form,
            'tasks': tasks,
            'uncompleteCount': uncompleteCount,
        })

    def POST(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        # else invalid... @todo implement

# class TaskView(RestView):

#     def GET(self, request, task_id):
#         pass

#     def PUT(self, request, task_id):
#         pass

#     def DELETE(self, request, task_id):
#         pass

