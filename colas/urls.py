from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_colas, name='colas'),
    path('<int:cola_id>/', views.product_page, name='product_page'),
    path('add/', views.add_cola, name='add_cola'),
    path('edit/<int:cola_id>/', views.edit_cola, name='edit_cola'),
]
