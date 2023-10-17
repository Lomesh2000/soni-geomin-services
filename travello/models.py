from django.db import models

# Create your models here.

class Destination(models.Model):
    # id : int  
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics') 
    desc = models.TextField() 
    price = models.IntegerField() 
    offer = models.BooleanField(default=False)


class Projects(models.Model):
    company_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='projects_pics')
    desc = models.TextField()
    equipments_used = models.TextField()
    
    