from django.shortcuts import render, redirect
from cart.models import Cart, CartItem
from .models import Order, OrderItem
from django.utils import timezone
from datetime import timedelta


def create_order(request):
    cart = get_object_or_404(Cart, customer=request.user.customer)
    if not cart.cartitem_set.exists():
        return redirect('cart_detail')

    # Создаём заказ
    order = Order.objects.create(
        customer=request.user.customer,
        total_price=sum(item.dish.price * item.quantity for item in cart.cartitem_set.all()),
        delivery_time=timezone.now() + timedelta(hours=1),
        status='new'
    )

    # Переносим товары из корзины в заказ
    for cart_item in cart.cartitem_set.all():
        OrderItem.objects.create(
            order=order,
            dish=cart_item.dish,
            quantity=cart_item.quantity,
            item_price=cart_item.dish.price
        )

    # Очищаем корзину
    cart.cartitem_set.all().delete()
    return render(request, 'orders/success.html', {'order': order})


def order_history(request):
    orders = Order.objects.filter(customer=request.user.customer).order_by('-created_at')
    return render(request, 'orders/history.html', {'orders': orders})