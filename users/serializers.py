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




