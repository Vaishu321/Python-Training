from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
import json

@csrf_exempt
def product(request):

    # GET ALL PRODUCTS
    if request.method == "GET":
        data = list(Product.objects.values())
        return JsonResponse(data, safe=False)

    # CREATE PRODUCT
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))
        Product.objects.create(
            name=body["name"],
            brand=body["brand"],
            price=body["price"]
        )
        return JsonResponse({"message": "POST EXECUTED"})

    # UPDATE EMPLOYEE (expect id in JSON)
    if request.method == "PUT":
        body = json.loads(request.body.decode('utf-8'))
        prod = Product.objects.get(id=body["id"])
        prod.name = body["name"]
        prod.brand = body["brand"]
        prod.price = body["price"]
        prod.save()
        return JsonResponse({"message": "PUT EXECUTED"})

    # DELETE EMPLOYEE (expect id in JSON)
    if request.method == "DELETE":
        body = json.loads(request.body.decode('utf-8'))
        prod = Product.objects.get(id=body["id"])
        prod.delete()
        return JsonResponse({"message": "DELETE EXECUTED"})

    return JsonResponse({"error": "Method not allowed"}, status=405)
