from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from phonenumber_field.modelfields import PhoneNumberField

class Customer(models.Model):
    customer_name=models.CharField(max_length=100)
    customer_phone=PhoneNumberField(unique=True)
    customer_address=models.CharField(max_length=250)

    def __str__(self):
        return self.customer_name

class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_brand=models.CharField(max_length=100)
    product_code=models.CharField(max_length=20,unique=True)
    product_price=models.IntegerField()
    product_sales=models.IntegerField()

    def __str__(self):
        return self.product_name

class Employee(AbstractUser):
    employee_address=models.CharField(max_length=250)
    employee_phone=PhoneNumberField()
    employee_name=models.CharField(max_length=100,default="")
    employee_id_type=models.CharField(max_length=50)
    employee_id_number=models.CharField(max_length=20)
    employee_sales=models.IntegerField(default=0)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='employee_groups', 
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='employee_user_permissions',  
        blank=True,
        help_text='Specific permissions for this user.'
    )
    

class Bill(models.Model):
    billing_employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    customer_billed=models.ForeignKey(Customer,on_delete=models.CASCADE)
    sold_products=models.ManyToManyField(Product)
    total_price=models.IntegerField()
    received_amount=models.IntegerField()
    return_amount=models.IntegerField()
