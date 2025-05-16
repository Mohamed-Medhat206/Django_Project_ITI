from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from product.models import Product

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        Category.objects.create(name=name, description=description)
        return redirect('category:list')
    return render(request, 'category/create.html')

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.description = request.POST.get('description')
        category.save()
        return redirect('category:list')
    return render(request, 'category/edit.html', {'category': category})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category:list')
    return render(request, 'category/delete.html', {'category': category})