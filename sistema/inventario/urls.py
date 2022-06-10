from django.urls import path
from . import views

app_name = "inventario"

urlpatterns = [
    path('register/', views.UserRegister.as_view(), name="user-register"),
    
]