from django.shortcuts import render, redirect, HttpResponse

def index(request):
    products = load_products("load")    
    return render(request, 'cart/index.html', {'products': products} )


def checkout(request):
    return render(request, 'cart/checkout.html')


def process_order(request):
    product_id = int(request.POST['product_id'])
    quantity = int(request.POST['quantity'])
    
    for product in load_products("search"):
        if product['id'] == product_id:    
            price = product['price']
    
    request.session['order_total'] = price * quantity
    request.session['total_items'] = request.session.setdefault('total_items', 0) + quantity
    request.session['total_spent'] = request.session.setdefault('total_spent', 0) + request.session['order_total']

    return redirect('/checkout')


def load_products(method):
    products = [{'id': 1, 'name': "DojoTshirt", 'price': 19.99}, 
                {'id': 2, 'name': "DojoSweater", 'price': 29.99}, 
                {'id': 3, 'name': "DojoCup", 'price': 4.99}, 
                {'id': 4, 'name': "Algorithm Book", 'price': 49.99}, 
                {'id': 5, 'name': "DojoHat", 'price': 14.99}, 
                ]
    
    if method == "load":
        return products
    
    def iter_func():
        for i in range(len(products)):
            yield products[i]
    return iter_func()


def clear(request):
    del request.session['order_total'] 
    del request.session['total_items'] 
    del request.session['total_spent']
    return redirect('/')