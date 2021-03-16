from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        'all_products': Product.objects.all()
    }
    return render(request, 'store/index.html', context)


def checkout(request):
    quantity_from_form = int(request.POST['quantity'])
    price_from_form = float(Product.objects.get(id=request.POST['productID']).price)
    total_charge = quantity_from_form * price_from_form
    print('Charging credit card...')
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    request.session['lastCharge'] = total_charge
    return redirect('/thankyou')
#    return render(request, "store/checkout.html")

def thankyou(request):
    orders = Order.objects.all()
    totalCharge = 0
    numItems = 0
    for order in orders:
        totalCharge += order.total_price
        numItems += order.quantity_ordered
    context = {
        "total": totalCharge,
        "numItems": numItems,
        "lastCharge": request.session['lastCharge'],
    }
    return render(request, "store/checkout.html", context)
