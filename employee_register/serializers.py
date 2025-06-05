from rest_framework import serializers
from .models import Employee,Emp

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = '__all__'
