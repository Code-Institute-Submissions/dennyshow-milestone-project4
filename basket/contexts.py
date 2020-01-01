from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):
    
    basket = request.session.get('basket', {})
    
    
    basket_items = []
    total = 0
    product_count = 0
    for id, quantity in basket_items:
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.end_time
        product_count += quantity
        basket_items.append({'id':id, 'quantity': quantity, 'product': product })
        
    return { 'basket_items': basket_items, 'total': total, 'product_count': product_count }