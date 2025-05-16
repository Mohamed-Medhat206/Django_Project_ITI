from django.shortcuts import render, get_object_or_404
from .models import Category

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/list.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    return render(request, 'category/detail.html', {
        'category': category,
        'product': products
    })