from django.urls import path, include
from .views import (
    PassengerListApiView,
    PassengerDetailApiView
)

urlpatterns = [
    path('passengers', PassengerListApiView.as_view()),
    path('passengers/<int:passenger_id>', PassengerDetailApiView.as_view()),
]