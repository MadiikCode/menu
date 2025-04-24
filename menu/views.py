from django.shortcuts import render
from .models import Dish, Category

def menu_list(request):
    categories = Category.objects.all()
    return render(request, 'menu/menu_list.html', {'categories': categories})

def create_order(request):
    if request.method == 'POST':
        # Здесь будет обработка заказа (сохранение в БД)
        return render(request, 'menu/order_success.html')
    return render(request, 'menu/order_form.html')