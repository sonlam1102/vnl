from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'provinces/', ProvinceView.as_view()),
    url(r'districts/', DistrictView.as_view()),
    url(r'wards/', WardView.as_view()),
]