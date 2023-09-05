from django.urls import path
from . import views

urlpatterns = [
    path("catalog",views.catalog, name = "catalog"),
    path("products/<int:id>/",views.products, name = "products"),
    path("product/<int:ids>/",views.product_car, name = "product_car"),
    path("",views.personal_area, name = "personal_area"),
    path(r'register/', views.register, name='register'),
    path(r'login/', views.Login_sing, name='login'),
    path(r'changing_user_data/', views.changing_user_data, name='changing_user_data'),
    path("shopping_cart",views.shopping_cart, name = "shopping_cart"),
    path("add_shopping_cart/<int:ids>/",views.add_shopping_cart, name = "add_shopping_cart"),
    path("order_user_data/",views.order_user_data, name = "order_user_data"),

]
