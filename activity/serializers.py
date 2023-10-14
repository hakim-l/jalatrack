from rest_framework import serializers
from .models import ActivityModel
import datetime

class activitySerializer(serializers.ModelSerializer):
    class Meta:
        model= ActivityModel
        fields= ('id','started_at','end_at','plan_id')

    def create(self, validated_data):
        end_at= datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        activity= validated_data['activity']
        activity_type= validated_data['activity_type']

        model= ActivityModel()
        model.activity= activity
        model.end_at= end_at
        model.activity_type= activity_type
        model.save()
        return model

    def update(self, instance, validated_data):
        instance.activity= validated_data.get('activity')
        instance.activity_type= validated_data.get('activity_type')
        instance.save()
        return instance


