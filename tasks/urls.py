from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'tasks.views.get', name="tasks_views_get"),
)
