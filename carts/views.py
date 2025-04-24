from django.shortcuts import render, redirect
from .models import Cart, CartItem
from menu.models import Dish

def add_to_cart(request, dish_id):
    dish = Dish.objects.get(id=dish_id)
    cart, created = Cart.objects.get_or_create(customer=request.user.customer)
    CartItem.objects.create(cart=cart, dish=dish, quantity=1)
    return redirect('menu_list')

def cart_detail(request):
    cart = Cart.objects.filter(customer=request.user.customer).first()
    return render(request, 'cart/detail.html', {'cart': cart})
