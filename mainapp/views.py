from django.shortcuts import render
from .models import ProductCategory, Product

def index(request):
    context = {
        'title': 'Main page',
        'name': 'GeekShop Store',
        'description': 'Новые образы и лучшие бренды на GeekShop Store.Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    products_data = Product.objects.all()
    categories_data = ProductCategory.objects.all()
    context = {
        'title': 'Main page',
        'name': 'GeekShop Store',
        'categories': categories_data,
        'slides': [
            {'img': 'vendor/img/slides/slide-1.jpg', 'pic_alt': 'First slide'},
            {'img': 'vendor/img/slides/slide-2.jpg', 'pic_alt': 'Second slide'},
            {'img': 'vendor/img/slides/slide-3.jpg', 'pic_alt': 'Third slide'},
        ],
        'products': products_data
    }

    return render(request, 'mainapp/products.html', context)
