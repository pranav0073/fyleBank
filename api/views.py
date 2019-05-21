
import json
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Bank, Branch
from rest_framework.decorators import api_view
from .serializers import BankSerializer, BranchSerializer
from rest_framework import viewsets
from .seedutil import insertBank


def index(request):
    
    
    return HttpResponse("Welcome")


@api_view(["GET"])
def test(request):
    insertBank()
    return HttpResponse("test")
   
    

@api_view(["GET"])
def banklist(request):
    bank_name = request.GET.get('name')
    city_name = request.GET.get('city')
    if request.method == 'GET':
        
        if bank_name == None or city_name == None:
            objs = Bank.objects.all()
            __serializer = BankSerializer(objs, many=True)
            return JsonResponse(__serializer.data, safe=False)
        else:
            obj = Bank.objects.filter(name=bank_name)
            if not len(obj)<1:
                branch = Branch.objects.filter( city=city_name, bank_id=obj[0])
                __serializer = BranchSerializer(branch, many=True)
                return JsonResponse(__serializer.data, safe=False)
            else:
                return HttpResponse("No such Bank Found")

@api_view(["GET"])
def bankDetail(request,pk):
    if request.method == 'GET':
        try:
            objs = Bank.objects.get(id=pk)
            __serializer = BankSerializer(objs)
            return JsonResponse(__serializer.data)
        except Bank.DoesNotExist:
            return HttpResponse(status=404)    
        
@api_view(["GET"])
def branchList(request):
    if request.method == 'GET':
        objs = Branch.objects.all()[:1000]
        __serializer = BranchSerializer(objs, many=True)
        return JsonResponse(__serializer.data, safe=False)

@api_view(["GET"])
def branchDetail(request,pk):
    if request.method == 'GET':
        try:
            objs = Branch.objects.get(ifsc=pk)
            __serializer = BranchSerializer(objs)
            return JsonResponse(__serializer.data)
        except Branch.DoesNotExist:
            return HttpResponse(status=404)   
    
# Create your views here.
