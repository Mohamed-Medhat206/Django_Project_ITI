# product/forms.py
from django import forms
from .models import *
from category.models import Category
from django.shortcuts import get_object_or_404


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image']



class ProductFormHandler:
    @staticmethod
    def handle_edit_form(request, product):
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.category = get_object_or_404(Category, pk=request.POST.get('category'))
        
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        
        product.save()
        return product