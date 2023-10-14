from django.db import models

# Create your models here.
class DivisionModel(models.Model):
    id= models.AutoField(primary_key= True)
    name= models.CharField(max_length=255)

    def __str__(self):
        return self.name
    class Meta:
        db_table= 'divisions'
