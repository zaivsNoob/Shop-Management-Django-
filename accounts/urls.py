from django.urls import path
from . import views




urlpatterns = [
    path("",views.home,name='home'),
    path("products/",views.product,name='products'),
    path("customer/<str:pk>",views.customer,name='customer'),
    path("create/",views.createOrder,name='create_order'),
    path("update_order/<str:pk>",views.updateOrder,name='update'),
    path("delete_order/<str:pk>",views.deleteOrder,name='delete'),
    path("login/",views.loginUser,name="login"),
    path("register/",views.registerUser,name="register"),
    path("logout/",views.logoutUser,name="logout")
]
