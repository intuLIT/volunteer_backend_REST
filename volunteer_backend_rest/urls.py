from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = [
    url(r'^user/info/$', views.UserDetail.as_view(), name="info"),
    url(r'^event/nearby/$', views.EventsNearbyList.as_view(), name="nearby"),
    url(r'^event/all/$', views.EventsAll.as_view(), name="events"),
    url(r'^create_event', views.CreateEvent.as_view()),
    url(r'^add_user', views.UserSignUp.as_view()),
    url(r'^convert_id',views.ConvertId.as_view()),
    url(r'^convert_event', views.ConvertEventId.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)