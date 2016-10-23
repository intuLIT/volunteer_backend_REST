from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = [
    url(r'^user/info/$', views.UserDetail.as_view(), name="info"),
    url(r'^event/nearby/$', views.EventsNearbyList.as_view(), name="nearby"),
    # url(r'^event/create/$', views.CreateEvent.as_view(), name="eventCreate"),
]

urlpatterns = format_suffix_patterns(urlpatterns)