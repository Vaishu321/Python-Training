# from django.http import JsonResponse, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
#
# @csrf_exempt
# def employees(request):
#     if request.method == "GET":
#         return JsonResponse({"message": "GETTING REQUEST"})
#     if request.method == "POST":
#         return JsonResponse({"message": "POST REQUEST"})
#     if request.method == "PUT":
#         return JsonResponse({"message": "PUT REQUEST"})
#     if request.method == "DELETE":
#         return JsonResponse({"message": "DELETE REQUEST"})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employees
import json

@csrf_exempt
def employees(request):

    # GET ALL EMPLOYEES
    if request.method == "GET":
        data = list(Employees.objects.values())
        return JsonResponse(data, safe=False)

    # CREATE EMPLOYEE
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))
        Employees.objects.create(
            name=body["name"],
            role=body["role"],
            salary=body["salary"]
        )
        return JsonResponse({"message": "POST EXECUTED"})

    # UPDATE EMPLOYEE (expect id in JSON)
    if request.method == "PUT":
        body = json.loads(request.body.decode('utf-8'))
        emp = Employees.objects.get(id=body["id"])
        emp.name = body["name"]
        emp.role = body["role"]
        emp.salary = body["salary"]
        emp.save()
        return JsonResponse({"message": "PUT EXECUTED"})

    # DELETE EMPLOYEE (expect id in JSON)
    if request.method == "DELETE":
        body = json.loads(request.body.decode('utf-8'))
        emp = Employees.objects.get(id=body["id"])
        emp.delete()
        return JsonResponse({"message": "DELETE EXECUTED"})

    return JsonResponse({"error": "Method not allowed"}, status=405)
