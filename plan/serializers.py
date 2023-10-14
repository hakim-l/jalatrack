from rest_framework import serializers
from .models import PlanModel
import datetime

class planSerializers(serializers.ModelSerializer):
    class Meta:
        model= PlanModel
        fields= ('id','name','email','surpervisor_employee_id',
                 'is_supervisor','division_id','position_name')

    def create(self, validated_data):
        name= validated_data.get('name',"pororo")
        email= validated_data.get('email','pororo@gmail.com')
        supervisor_employee_id= validated_data.get('surpervisor_employee_id',0)
        is_supervisor= validated_data.get('is_supervisor',False)
        division_id= validated_data.get('division_id')
        position_name= validated_data.get('position_name')

        model= PlanModel()
        model.name= name
        model.email= email
        model.surpervisor_employee_id= supervisor_employee_id
        model.is_supervisor= is_supervisor
        model.division_id= division_id
        model.position_name= position_name

        model.save()
        return model

    def update(self, instance, validated_data):
        name = validated_data.get('name', "pororo")
        email = validated_data.get('email', 'pororo@gmail.com')
        supervisor_employee_id = validated_data.get('surpervisor_employee_id', 0)
        is_supervisor = validated_data.get('is_supervisor', False)
        division_id = validated_data.get('division_id')
        position_name = validated_data.get('position_name')

        instance.name = name
        instance.email = email
        instance.surpervisor_employee_id = supervisor_employee_id
        instance.is_supervisor = is_supervisor
        instance.division_id = division_id
        instance.position_name = position_name

        instance.save()
        return instance

