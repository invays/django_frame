from django.shortcuts import render


def index(request):
    context = {
        'title': 'Main page',
        'name': 'GeekShop Store',
        'description': 'Новые образы и лучшие бренды на GeekShop Store.Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.'
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    context = {
        'title': 'Main page',
        'name': 'GeekShop Store',
        'categories': [
            {'name': 'Новинки'},
            {'name': 'Одежда'},
            {'name': 'Обувь'},
            {'name': 'Аксессуары'},
            {'name': 'Подарки'},
        ],
        'slides': [
            {'img': 'vendor/img/slides/slide-1.jpg', 'pic_alt': 'First slide'},
            {'img': 'vendor/img/slides/slide-2.jpg', 'pic_alt': 'Second slide'},
            {'img': 'vendor/img/slides/slide-3.jpg', 'pic_alt': 'Third slide'},
        ],
        'products': [
            {
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'image': 'vendor/img/products/Adidas-hoodie.png',
                'price': '6090,00',
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
            },
            {
                'name': 'Синяя куртка The North Face',
                'image': 'vendor/img/products/Blue-jacket-The-North-Face.png',
                'price': '23 725,00',
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
            },
            {
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'image': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                'price': '3 390,00',
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
            },
            {
                'name': 'Черный рюкзак Nike Heritage',
                'image': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
                'price': '2 340,00',
                'description': 'Плотная ткань. Легкий материал.',
            },
            {
                'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                'image': 'vendor/img/products/Black-Dr-Martens-shoes.png',
                'price': '13 590,00',
                'description': 'Гладкий кожаный верх. Натуральный материал',
            },
            {
                'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                'image': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
                'price': '2 890,00',
                'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
            }
        ]
    }

    return render(request, 'mainapp/products.html', context)
