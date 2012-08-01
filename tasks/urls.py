from django.conf.urls import patterns, include, url
from views import TaskIndexView, TaskView

urlpatterns = patterns('',

    url(r'^$', TaskIndexView.as_view(), name="task_index"),
    url(r'^(\d+)$', TaskView.as_view(), name="task"),
)
