from django.urls import path
from . import views




urlpatterns = [
    path("",views.home,name='home'),
    path("products/",views.product,name='products'),
    path("customer/<str:pk>",views.customer,name='customer'),
    path("creat/",views.createOrder,name='create_order'),
    path("update_order/<str:pk>",views.updateOrder,name='update'),
    path("delete_order/<str:pk>",views.deleteOrder,name='delete')

]
