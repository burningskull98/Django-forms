from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductModelForm
from django.contrib import messages
from django.shortcuts import redirect


def index(request):
    return render(request, 'shop_app/base.html')

def product_list(request):
    products = Product.objects.all()
    context = {
        'product_list': products,
    }
    return render(request, 'shop_app/product_list.html', context=context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'shop_app/product_detail.html', context=context)


def create_product(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Товар успешно создан')
            return redirect('product_list')
    else:
        form = ProductModelForm()
    return render(request, 'shop_app/create_product.html', {'form': form, 'title': 'Создать товар'})


def edit_product(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductModelForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Товар успешно обновлен')
            return redirect('product_list', )
    else:
        form = ProductModelForm()
    return render(request, 'shop_app/edit_product.html', {'form': form, 'title': 'Редактировать товар'})
