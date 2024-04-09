from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields='__all__'
    
    def validate(self,data):
        if Product.objects.filter(product_code=data['product_code']).exists():
            raise serializers.ValidationError('Product code should be unique')
        
        return data
    
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'

    def validate(self,data):
        numbers="0123456789!#$%&'()*+,-./:;<=>?@[\]^_{|}~"
        if any(c in numbers for c in data['customer_name']):
            raise serializers.ValidationError('The name of the customer cannot have any special character or numerics')
        length=len(data['customer_phone'])
        if Customer.objects.filter(customer_phone=data['customer_phone']).exists():
            raise serializers.ValidationError('This phone number is already registered')
        return data
    

class EmploySerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bill
        fields=['received_amount']

class BillView(serializers.ModelSerializer):
    class Meta:
        model=Bill
        fields='__all__'
        

