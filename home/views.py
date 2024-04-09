from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.db.models import Max
from rest_framework_simplejwt.authentication import JWTAuthentication

class ProductViewAdd(generics.ListAPIView,generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ProductUpdateDelete(generics.DestroyAPIView,generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='product_code'

class CustomerViewAdd(generics.ListAPIView,generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

class CustomerUpdateDelete(generics.DestroyAPIView,generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    lookup_field='customer_phone'

class EmployeeView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset=Employee.objects.all()
    serializer_class=EmploySerializer

class EmployeeDelete(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset=Employee.objects.all()
    serializer_class=EmploySerializer
    lookup_field='id'

class BillingDescription(generics.ListAPIView):
    queryset=Bill.objects.all()
    serializer_class=BillView

class Billing(GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = BillSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data=request.data
            products = data['products']
            employee = request.user.username
            customer = data['customer']
   
            commodities = []
   
            for product in products:
                commodity = Product.objects.get(product_code=product)
                commodity.product_sales += 1
                commodities.append(commodity)
                commodity.save()
   
            total = sum(commodity.product_price for commodity in commodities)
               
            emp = Employee.objects.get(username=employee)
            emp.employee_sales += total
            emp.save()
            buyer = Customer.objects.get(id=customer)
            received_amount = data['received_amount']
            return_amount = received_amount - total
            ins = Bill.objects.create(billing_employee=emp, customer_billed=buyer, total_price=total, received_amount=received_amount, return_amount=return_amount)
            ins.sold_products.set(commodities)
            return Response({"message": "Your products are billed successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class OtherFeatures(GenericAPIView):
    def post(self,request):
        best_employee = Employee.objects.annotate(max_value=Max('employee_sales')).order_by('-max_value').first()
        max_sales=best_employee.username
        best_product = Product.objects.annotate(max_value=Max('product_sales')).order_by('-max_value').first()
        max_sold=best_product.product_name

        return Response({"The employee with most item sold is: ",max_sales,"The most sold product is: ",max_sold})



