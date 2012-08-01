from django.conf.urls import patterns, include, url
from views import TaskIndexView

urlpatterns = patterns('',

    url(r'^$', TaskIndexView.as_view(), name="task_index"),
)
