# Create your views here.
import json

from django.http import JsonResponse

from .api import products

product_handler = products()


def update_product(request):
    print(product_handler.update_product(int(request.POST['id']), {"regular_price": request.POST['regular_price']}))
    return JsonResponse({'success': True})


def update_products(request):
    result = product_handler.update_products(json.loads(request.POST["product_data"])).text

    return JsonResponse({'success': True, 'result': result})
