from django.db import models
from division.models import DivisionModel
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
#https://learndjango.com/tutorials/django-custom-user-model
# Create your models here.

class EmployeeModel(AbstractUser):
    id = models.AutoField(unique=True,
                          primary_key=True,
                          )
    username= models.CharField(max_length=255,
                           null=False,
                               unique=True
                           )

    # password = models.CharField(max_length=255,
    #                             null=False
    #                             )
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

    def __str__(self):
        return self.username

    class Meta:
        db_table= 'employees'

    def get_employee(self,id):
        return (self.id==id)
