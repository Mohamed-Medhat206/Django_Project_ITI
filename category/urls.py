from django.urls import path
from . import views

app_name = 'category'

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('create/', views.category_create, name='create'),
    path('edit/<int:pk>/', views.category_edit, name='edit'),
    path('delete/<int:pk>/', views.category_delete, name='delete'),
]