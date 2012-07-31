from django.conf.urls import patterns, include, url
from views import TaskIndexView

urlpatterns = patterns('',

    url(r'^$', TaskIndexView(), name="task_index"),
)
