# Create your views here.
from django.shortcuts import render
from forms import TaskForm


def index(request):
	form = TaskForm()
	return render(request, 'tasks/index.html', {"name": "World", "form": form})