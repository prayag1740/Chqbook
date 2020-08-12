import json
import requests
import traceback

from rest_framework import status as http_status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db import transaction
from django.conf import settings
from razorpay.config import Config
from razorpay.models import Orders, OrderNoteMapping
from pc_rpcb.logging import AppLogger

logger = AppLogger(tag="razorpay views")

class CreateOrder(APIView):
    
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        
        amount = request.data.get("amount")
        currency = request.data.get("currency", "INR")
        receipt = request.data.get("receipt")
        payment_capture = request.data.get("payment_capture",1)
        notes = request.data.get("notes")
        
        if amount is None:
            err = Config.MISSING.AMOUNT
            response = {"status": err[0], "message": err[1]}
            return Response(response, status=http_status.HTTP_400_BAD_REQUEST)
        
        
        logger.info(f"making request to razorpay api for creating order")
        
        try:
            payload = {
                "amount" : amount,
                "currency" : currency,
                "receipt" : receipt,
                "payment_capture": payment_capture,
                "notes" : notes if notes else {}
            }
            razorpay_username = settings.RAZOREPAY_USERNAME
            razorpay_password = settings.RAZOREPAY_PASSWORD
            razorpay_create_order_url = settings.RAZOREPAY_CREATE_ORDER_URL
            logger.info(f"request for creating order is {payload}")
            
            response = requests.post(url=razorpay_create_order_url, json=payload, auth=(razorpay_username, razorpay_password))
            response_status_code = response.status_code
            response_result = json.loads(response.content)
            logger.info("response code from razor pay create order is {response_status_code}")
            
            if response.status_code !=200:
                logger.error("some error occured while creating razorpay order")
                error = response_result.get("error")
                error_msg = error.get("description")
                response = {
                    "status" : 1,
                    "message" : error_msg
                }   
                return Response(response, status=http_status.HTTP_409_CONFLICT)
            else:
                logger.info("success in calling razorpay order api")
                order_id = response_result.get("id")
                amount = response_result.get("amount")
                amount_paid = response_result.get("amount_paid")
                amount_due = response_result.get("amount_due")
                offer_id = response_result.get("offer_id")
                status = response_result.get("status")
                notes = response_result.get("notes")
                
                order_class = Orders()
                create_status = order_class.CREATED
                create_order = Orders.objects.create(order_id=order_id, amount=amount, amount_paid=amount_paid, amount_due=amount_due, 
                                                     offer_id=offer_id, status=create_status)
                
                if notes:
                    description_list = []
                    for note_mapping in notes:
                        description_list.append(note_mapping.values())
                        for descriptions in description_list: 
                            OrderNoteMapping.objects.create(order_pk=create_order.id, description=descriptions)
                            
                response = {
                    "status" : Config.GENERIC.SUCCESS[0],
                    "message" : Config.GENERIC.SUCCESS[1],
                    "data" : {
                        "order_id" : order_id,
                        "maount" : amount,
                        "amount_paid" : amount_paid,
                        "amount_due" : amount_due,
                        "status" : status
                    }
                }
                
                return Response(response, status=http_status.HTTP_200_OK)
            
        except Exception as e:
            logger.error("some issue occured while creating order")
            logger.error(traceback.format_exc())
            
            response = {
                "status": Config.GENERIC.FAILURE[0],
                "message": Config.GENERIC.FAILURE[1]
            }
            
            return Response(response, status=http_status.HTTP_409_CONFLICT)
                

            
            
            
            
            
            
            
            
            
            
