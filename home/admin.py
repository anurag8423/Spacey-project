from django.contrib import admin
from .models import Customer,Product, Employee,Bill

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Employee)
admin.site.register(Bill)
