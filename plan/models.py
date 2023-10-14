from django.db import models
from employee.models import EmployeeModel
# Create your models here.

class PlanModel(models.Model):
    id= models.AutoField(unique=True,
                          primary_key=True
                         )

    employee_id = models.ForeignKey(EmployeeModel,
                                    on_delete=models.PROTECT
                                    )

    started_at= models.DateTimeField(null=False)
    end_at = models.DateTimeField(null=False)

    activity = models.CharField(max_length=255,
                                null=False
                                )
    activity_type = models.CharField(max_length=255,
                                     null=False
                                     )

    class Meta:
        db_table= 'plans'