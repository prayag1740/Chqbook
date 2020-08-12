from django.urls import path, include


urlpatterns = [
    path(r'chqbook/api/v1/', include(('razorpay.urls', 'razorpay'), namespace = 'v1'))
]
