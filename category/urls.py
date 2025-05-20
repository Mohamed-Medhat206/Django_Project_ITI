from django.urls import path
from . import views
from .views import (
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
)
app_name = 'category'

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('create/', views.category_create, name='create'),
    path('edit/<int:pk>/', views.category_edit, name='edit'),
    path('delete/<int:pk>/', views.category_delete, name='delete'),
    
    path('gv', CategoryListView.as_view(), name='category_list'),
    path('createg/', CategoryCreateView.as_view(), name='create'),
    path('editg/<int:pk>/', CategoryUpdateView.as_view(), name='edit'),
    path('deleteg/<int:pk>/', CategoryDeleteView.as_view(), name='delete'),
]



