from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    this_product = Product.objects.get(id=request.POST['product_id'])
    quantity_from_form = int(request.POST['quantity'])
    price = float(this_product.price)
    total_price = price * quantity_from_form
    new_order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_price)
    
    return redirect(f'/checkout/create/{new_order.id}')

def order(request, order_id):
    this_order = Order.objects.last()
    order_total = 0
    total_ordered = 0
    for order in Order.objects.all():
        order_total = order_total + order.total_price
        total_ordered = total_ordered + order.quantity_ordered
    
    
    context = {
        'this_order' : this_order,
        'quantity' : total_ordered,
        'order_total' : order_total
    }
    
    return render(request, "store/checkout.html", context)