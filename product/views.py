from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from category.models import Category
from .forms import ProductFormHandler 


def product_list(request):
    products = Product.getall()
    
    return render(request, 'product/list.html', {'products': products})


def product_create_MF(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid() and form.is_bound:
            form.save()
            return redirect('product:product_list')
    else:
        form = ProductForm()
    
    return render(request, 'product/create_mf.html', {'form': form})


def product_create(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        category = get_object_or_404(Category, pk=request.POST.get('category'))
        product = Product(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            price=request.POST.get('price'),
            category=category
        )
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.save()
        return redirect('product:product_list')
    return render(request, 'product/create.html', {'categories': categories})



def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = Category.objects.all()
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.category = get_object_or_404(Category, pk=request.POST.get('category'))
        
        if 'image' in request.FILES:
            product.image = request.FILES['image']
            
        product.save()
        return redirect('product:product_list')
    return render(request, 'product/edit.html', {'product': product, 'categories': categories})




def product_edit_f(request, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = Category.objects.all()
    
    if request.method == 'POST':
        ProductFormHandler.handle_edit_form(request, product)
        return redirect('product:product_list')
    
    return render(request, 'product/edit.html', {
        'product': product,
        'categories': categories
    })











def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.softdelete(pk)
    return redirect('product:product_list') 