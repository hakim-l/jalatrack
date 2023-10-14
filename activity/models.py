from django.db import models
from plan.models import PlanModel
from employee.models import EmployeeModel
from storage.storage import AlwaysOverwriteFileSystemStorage
from division.models import DivisionModel
# Create your models here.

choices=[
    ('visit','Visit'),
    ('meeting','Meeting'),
    ('project','Project')
]
class ActivityModel(models.Model):
    id = models.AutoField(unique=True,
                          primary_key=True
                          )
    employee= models.ForeignKey(EmployeeModel,
                                   on_delete=models.PROTECT
                                   )


    # started_at = models.DateTimeField(null=False)
    end_at = models.DateTimeField(null=False)
    plan= models.ForeignKey(PlanModel,
                               null=True,
                               on_delete=models.CASCADE
                               )
    activity= models.CharField(max_length=255,
                               null=False
                               )

    activity_type= models.CharField(max_length=255,
                                    null= False,
                                    choices=choices
                                    )

    attachment= models.FileField(storage=AlwaysOverwriteFileSystemStorage)

    division= models.ForeignKey(DivisionModel,
                                null= False,
                                on_delete=models.PROTECT
                                )
    percentage= models.FloatField(null=False)
    class Meta:
        db_table = 'activities'

# Create your models here.
