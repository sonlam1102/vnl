from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'provinces/$', ProvinceListView.as_view()),
    url(r'provinces/(?P<pk>\d+)', ProvinceObjectView.as_view()),

    url(r'districts/$', DistrictListView.as_view()),
    url(r'districts/(?P<pk>\d+)', DistrictObjectView.as_view()),

    url(r'wards/$', WardListView.as_view()),
    url(r'wards/(?P<pk>\d+)', WardObjectView.as_view()),
]