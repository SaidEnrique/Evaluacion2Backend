from django.shortcuts import render, get_object_or_404
from .models import Product, Category
def index(request):
    products = Product.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'products/index.html', {'products': products, 'categories': categories})
def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    categories = Category.objects.all()
    return render(request, 'products/category.html', {'category': category, 'products': products, 'categories': categories})
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = Category.objects.all()
    return render(request, 'products/detail.html', {'product': product, 'categories': categories})
