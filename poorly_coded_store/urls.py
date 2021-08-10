from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('checkout/<int:product_id>', views.checkout),
    path('checkout/create/<int:order_id>', views.order),
]

