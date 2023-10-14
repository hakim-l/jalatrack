from django.db import models
from division.models import DivisionModel
# Create your models here.

class EmployeeModel(models.Model):
    id = models.AutoField(unique=True,
                          primary_key=True,
                          )
    name= models.CharField(max_length=255,
                           null=False
                           )
    email= models.CharField(max_length=255,
                            null= False
                            )

    surpervisor_employee_id= models.IntegerField(primary_key=False,
                                                 null=True
                                                 )
    is_supervisor= models.BooleanField(default=False,
                                       )
    division_id= models.ForeignKey(DivisionModel,on_delete=models.CASCADE,
                                   null= False
                                   )
    position_name= models.CharField(max_length=255,
                                    null=False,
                                    default="intern")

    class Meta:
        db_table= 'employees'

    def get_employee(self,id):
        return (self.id==id)
