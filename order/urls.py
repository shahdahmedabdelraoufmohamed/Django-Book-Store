from django.urls import path
from . import views


urlpatterns = [
    path('orders/add-order/', views.add_order,name='add_order'), 
    path('orders/', views.get_orders,name='get_orders'), 
    path('orders/<int:pk>/', views.get_order,name='get_order'), 
  

]