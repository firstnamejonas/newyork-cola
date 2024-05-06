from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_items, name='add_items'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('delete/<item_id>/', views.delete_items, name='delete_items'),
]
