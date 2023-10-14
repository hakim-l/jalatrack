from rest_framework import serializers
from .models import EmployeeModel
import datetime

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= EmployeeModel
        fields= ('id','name','email','surpervisor_employee_id',
                 'is_supervisor','division_id','position_name')

    def create(self, validated_data):
        name= validated_data.get('name',"pororo")
        email=