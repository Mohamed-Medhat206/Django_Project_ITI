# product/forms.py
from django import forms
from .models import *
from category.models import Category
from django.shortcuts import get_object_or_404


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image']


