from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView
from sujets.models import Question
from sujets.views import vote


urlpatterns = patterns('',
	url(r'^$', ListView.as_view(model=Question)),
	url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Question), name='question_detail'),
	url(r'^vote/$', vote, name="vote")
)
