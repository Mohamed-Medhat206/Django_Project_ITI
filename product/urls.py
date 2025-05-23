from django.urls import path
from . import views
from .views import ProductListView
from .views import ProductDeleteView
from .api.views import *
from rest_framework.routers import DefaultRouter

app_name = 'product'

urlpatterns = [
    #api function based
    path('API/',getallpro,name='getallpro'),
    path('API/<int:id>',getbyid,name='getbyid'),


    path('plistview', ProductListView.as_view(), name='product_list'),
    path('', views.product_list, name='product_list'),
    path('create/', views.product_create, name='create'),
    path('create_fm/', views.product_create_MF, name='create'),
    path('edit/<int:pk>/', views.product_edit, name='edit'),
    path('edit_f/<int:pk>/', views.product_edit, name='edit'),
    # path('delete/<int:pk>/', views.product_delete, name='delete'),
    path('classdelete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
]