from django.shortcuts import render
from .models import *
# Create your views here.

def Homepage(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "store/home.html", context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)  #create an order or get an order if it exists
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0 } #incase the user is not logged in , temporarily setting it to false
    
    context = {'items':items, 'order':order}
    return render(request, "store/cart.html", context)
    