from rest_framework import serializers
from users.models import *

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ('__all__')

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('__all__')

class StudentsAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsAddress
        fields = ('__all__')

class StudentsDetailsAddressSerializer(serializers.ModelSerializer):
     students_address = StudentsAddressSerializer(many=True)
     class Meta:
        model = Student 
        fields = ('name','last_name','birth','mobile_number','students_address') 
        
     


