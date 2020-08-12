from django.urls import path, include
from razorpay import views as razor_pay_views


urlpatterns = [
     path(r'create-order/', razor_pay_views.CreateOrder.as_view())
]
