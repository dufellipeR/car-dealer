from django.urls import path

from .views import CarList, CarDetail

urlpatterns = [
    path('car/', CarList.as_view()),
    path('car/', CarDetail.as_view()),
]
