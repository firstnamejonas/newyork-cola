from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_colas, name='colas'),
    path('<cola_id>', views.product_page, name='product_page'),
]