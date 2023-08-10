from django.urls import path
from . import views

urlpatterns = [
    path("catalog",views.catalog, name = "catalog"),
    path("products/<int:id>/",views.products, name = "products"),
    path("product/<int:ids>/",views.product_car, name = "product_car"),
    path("personal_area/",views.personal_area, name = "personal_area"),
    path(r'register/', views.register, name='register'),
    path(r'login/', views.Login_sing, name='login'),
    path(r'changing_user_data/', views.changing_user_data, name='changing_user_data'),





]
