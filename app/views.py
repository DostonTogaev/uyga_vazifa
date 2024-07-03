from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.shortcuts import render
from django.db.models import Q
from app.forms import ProductModelForm, CommentModelForm, OrderModelForm
from app.models import Product, Category



# Create your views here.

def index_page(request, category_id=None):
    filter_type = request.GET.get('filter', '')
    search_query = request.GET.get('search', '')
    categories = Category.objects.all()
    if category_id:
        products = Product.objects.filter(category=category_id)
        if filter_type == 'expensive':
            products = products.order_by('-price')
        elif filter_type == 'cheap':
            products = products.order_by('price')
    else:
        products = Product.objects.all()
        if filter_type == 'expensive':
            products = products.order_by('-price')
        elif filter_type == 'cheap':
            products = products.order_by('price')

    if search_query:
        products = Product.objects.filter(
            Q(name__icontains=search_query) | Q(rating__icontains=search_query))

    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'app/home.html', context)


def product_detail_page(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    price_lower_bound = product.price * 0.8
    price_upper_bound = product.price * 1.2

    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)

    #related_products = Product.objects.filter(Q(price__lte=price_upper_bound) & Q(price__gte=price_lower_bound)).exclude(id=product_id)

    comments = product.comments.filter(is_active=True).order_by('-created_at')[:5]

    count = product.comments.count()
    context = {
        'product': product,
        'related_products': related_products,
        'comments': comments,
        'count': count
    }
    return render(request, 'app/detail.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = ProductModelForm()

    context = {
        'form': form,
    }
    return render(request, 'app/add-product.html', context)

def add_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    form = CommentModelForm()
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('product-detail', product_id)

    context = {
        'form': form,
        'product': product
    }

    return render(request, 'app/detail.html', context)

def expensive_product(request):
    products = Product.objects.filter(price__gt=50000)
    context = {
        'products': products,
    }
    return render(request, 'app/home.html', context)

def cheap_product(request):
    products = Product.objects.filter(price__lt=50000)
    context = {
        'products': products,
    }
    return render(request, 'app/home.html', context)

def add_order(request, product_id):
    product = Product.objects.filter(id=product_id).first()  # [1]
    form = OrderModelForm()
    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('product_detail', product.id)

    context = {
        'product': product,
        'form': form
    }

    return render(request, 'app/detail.html', context)

def delete_product(request, pk):
    product = Product.objects.filter(id=pk).first()
    if product:
        product.delete()
        return redirect('index')

    context = {
        'product': product,
    }
    return render('app/detail.html', context)


def edit_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductModelForm(instance=product)
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-detail', product.id)

    context = {
        'form': form,
        'product': product
    }
    return render(request, 'app/update.html', context)
