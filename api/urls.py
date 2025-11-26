from django.urls import path
from .views import get_menu, update_availability, place_order

urlpatterns = [
    path('menu', get_menu),
    path('update/<int:id>', update_availability),
    path('order', place_order),
]
