from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('edit/<int:pk>/', views.edit_item, name='edit_item'),
  path('delete/<int:pk>/', views.delete_item, name='delete_item'),
  path('toggle/<int:pk>/', views.toggle_check, name='toggle_check'),
]