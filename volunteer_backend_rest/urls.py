from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = [
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^create_event', views.CreateEvent.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)