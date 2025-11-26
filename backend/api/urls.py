from django.urls import path
from .views import get_menu, update_availability, place_order



from .views import home, get_menu, place_order, update_availability
from django.urls import path
from .views import get_menu, place_order, update_availability, home, login_user
from .views import home, get_menu, place_order, update_availability, login_user, signup_user



urlpatterns = [
    path('', home),                # <--- add this line
    path('menu', get_menu),
    path('order', place_order),
    path('update/<int:id>', update_availability),
    path("login", login_user),
    path("signup", signup_user),


]
