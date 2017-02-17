from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^candidate/add/$', views.index, name='index'),
   url(r'^candidateName/$', views.candidateName, name='candidateName'),
   url(r'^candidateList/$', views.candidateList, name='candidateList'),
   url(r'^candidateDetails/(?P<id>\d+)/$', views.candidateDetails, name='candidateDetails'),
]
