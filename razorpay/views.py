from django.conf import settings
from requests.auth import BasicAuth
from razorpay.config import Config
from razorpay.models import Orders, OrderNoteMapping


class CreateOrder(APIView):
    
    def post(self, request, *args, **kwargs):
        
        amount = request.data.get("amount")
        currency = request.data.get("currency", "INR")
        receipt = request.data.get("receipt")
        payment_capture = request.data.get("payment_capture",1)
        notes = request.data.get("notes")
        
        if amount is None:
            err = Config.MISSING.AMOUNT
            response = {"status": err[0], "message": err[1]}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
        
        logger.info(f"making request to razorpay api for creating order")
        
        try:
            payload = {
                "amount" : amount,
                "currency" : currency,
                "receipt" : receipt,
                "payment_capture": : payment_capture,
                "notes" : notes if notes else {}
            }
            razorpay_username = settings.RAZOREPAY_USERNAME
            razorpay_password = settings.RAZOREPAY_PASSWORD
            razorpay_create_order_url = settings.
            
            logger.info(f"request for creating order is {payload}")
            
            
            
            
            
            
            
            
