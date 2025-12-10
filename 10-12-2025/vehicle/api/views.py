from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Vehicle
import json

@csrf_exempt
def vehicle(request):

    # GET ALL PRODUCTS
    if request.method == "GET":
        data = list(Vehicle.objects.values())
        return JsonResponse(data, safe=False)

    # CREATE PRODUCT
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))
        Vehicle.objects.create(
            number_plate=body["number_plate"],
            vehicle_type=body["vehicle_type"],
            manufacturer=body["manufacturer"],
            year=body["year"]
        )
        return JsonResponse({"message": "POST EXECUTED"})

    # UPDATE EMPLOYEE (expect id in JSON)
    if request.method == "PUT":
        body = json.loads(request.body.decode('utf-8'))
        vehi = Vehicle.objects.get(id=body["id"])
        vehi.number_plate = body["number_plate"]
        vehi.vehicle_type = body["vehicle_type"]
        vehi.manufacturer = body["manufacturer"]
        vehi.year = body["year"]
        vehi.save()
        return JsonResponse({"message": "PUT EXECUTED"})

    # DELETE EMPLOYEE (expect id in JSON)
    if request.method == "DELETE":
        body = json.loads(request.body.decode('utf-8'))
        vehi = Vehicle.objects.get(id=body["id"])
        vehi.delete()
        return JsonResponse({"message": "DELETE EXECUTED"})

    return JsonResponse({"error": "Method not allowed"}, status=405)
