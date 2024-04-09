from django.urls import path
from home.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('productview/',ProductViewAdd.as_view()),
    path('productupdel/<product_code>/',ProductUpdateDelete.as_view()),
    path('customerviewadd/',CustomerViewAdd.as_view()),
    path('customerupdel/<id>/',CustomerUpdateDelete.as_view()),
    path('employeeview/',EmployeeView.as_view()),
    path('employeedel/<id>/',EmployeeDelete.as_view()),
    path('billing/',Billing.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('otherfeatures',OtherFeatures.as_view()),
    path('billview/',BillingDescription.as_view())
]
