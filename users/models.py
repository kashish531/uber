from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length= 15,null=True,blank=True)
    last_name = models.CharField(max_length=12,null=True,blank=True)
    birth = models.DateField(max_length=8,null=True,blank=True)
    mobile_number = models.IntegerField(max_length=10,null=True,blank=True)
    
    Gender= (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Others'),
    )

    Gender = models.IntegerField(
        choices = Gender,
        default= 1
    )
    def __str__(self):
        return str(self.name)
    

class Orders(models.Model):
    order_name = models.CharField(max_length= 15,null=True,blank=True) 
    order_price = models.IntegerField(max_length= 15,null=True,blank=True)
    order_discount = models.IntegerField(max_length= 15,null=True,blank=True)
    order_quentity = models.IntegerField(max_length= 15,null=True,blank=True)
    order_adderss = models.TextField(max_length= 15,null=True,blank=True)
    order_place_at = models.DateField(max_length= 15,null=True,blank=True)

class StudentsAddress(models.Model):
    Student = models.ForeignKey(Student,on_delete= models.CASCADE,null=True)
    street_name = models.CharField(max_length=60,null=True,blank=True)
    house_no = models.IntegerField(max_length=60,null=True,blank=True)
    city = models.CharField(max_length=60,null=True,blank=True)
    state = models.CharField(max_length=60,null=True,blank=True)
    country = models.CharField(max_length=60,null=True,blank=True)
    pincode = models.IntegerField(max_length=60,null=True,blank=True)
 
    def __str__(self):
        return str(self.street_name)