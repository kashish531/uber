from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework .response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import *
from users.serializers import *


class GetStudentView(APIView):
    def get(self,request):
        print("req",request.GET)
        name = request.GET.get("myname")
        print("name",name)
        if name:
            instance = Student.objects.filter(name=name)
        else :
            instance = Student.objects.all()   
        serializers = StudentSerializer(instance,many= True)
        return Response(data = serializers.data)
    
    def post(self,request):
        params = request.data
        print("params",params)
        serializer = StudentSerializer(data=params)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message","done"})


class GetOrdersViews(APIView):
    def get(self,request):
        print("req",request.GET)
        order_name = request.GET.get("myname")
        print("name",order_name)
        if order_name:
            instance = Orders.objects.filter(name=order_name)
        else :
            instance = Orders.objects.all()   
        serializers =OrdersSerializer(instance,many= True)
        return Response(data = serializers.data)
    
    def post(self,request):
        params = request.data
        print("params",params)
        serializer = OrdersSerializer(data=params)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message","done"})
class DeleteStudentView(APIView):
    def get(self,request,pk):
        instance = Student.objects.get(id=pk)
        instance.delete()
        return Response({"Message","Delete"})
class DeleteOrdersViews(APIView):
    def get(self,request,pk):
        instance = Orders.objects.get(id=pk)
        instance.delete()
        return Response({"message","Delete"})

class StudentsDetailsAddressViews(APIView):
    def get (self,request,pk):
        instances = Student.objects.filter(id=pk)
        serializer =StudentsDetailsAddressSerializer(instances,many=True )
        return Response(serializer.data)
    
class StudentsAddressDeleteViews(APIView):
    def get(self,request,pk):
        instances = Student.objects.get(id=pk)
        address = StudentsAddress.objects.filter(Student=instances)
        address.delete()
        return Response({"delete sucessfully"})    

class StudentsUpdateViews(APIView):
    def post(self,request,pk):
        params = request.data
        print("------",params)
        student = Student.objects.filter(id=pk).update(**params)
        return Response({"updated"})
    