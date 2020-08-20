from django.utils import timezone
from django.db import models



class Orders(models.Model):
    
    CREATED = 0
    AUTHORIZED = 1
    CAPTURED = 2
    REFUNDED = 3
    FAILED = 4
    
    STATUS_CHOICE =(
        (CREATED, "Created"),
        (AUTHORIZED, "Authorized"),
        (CAPTURED, "Captured"),
        (REFUNDED, "Refunded"),
        (FAILED, "Failed"),
    ) 
    
    order_id = models.CharField(max_length=255, db_index=True)
    amount = models.PositiveIntegerField()
    amount_paid = models.PositiveIntegerField()
    amount_due = models.PositiveIntegerField()
    currency = models.CharField(max_length=10)
    receipt = models.CharField(max_length=255, null=True, blank=True)
    offer_id = models.PositiveIntegerField(null=True, blank=True)
    status = models.PositiveIntegerField(choices=STATUS_CHOICE, null=True, blank=True)
    attempts = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = "orders"
        
        
class OrderNoteMapping(models.Model):
    
    order_pk = models.PositiveIntegerField()
    note_description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
class Payment(models.Model):
    
    INITIATED = 0
    PROCESSING = 1
    REFUNDED = 2
    CANCELLED = 3
    
    REFUND_STATUS = (
        (INITIATED, "Initiated"),
        (PROCESSING, "Processing"),
        (REFUNDED, "Refunded"),
        (CANCELLED, "Cancelled"),
    )
    
    payment_id = models.CharField(max_length=255, db_index=True)
    order_id = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    invoice_id = models.CharField(max_length=255, null=True, blank=True)
    is_international = models.BooleanField(default=False)
    method = models.CharField(max_length=25)
    amount_refunded = models.PositiveIntegerField(default=0)
    refund_status = models.PositiveIntegerField(choices=REFUND_STATUS, null=True, blank=True)
    captured = models.PositiveIntegerField(default=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    wallet_id = models.PositiveIntegerField(null=True, blank=True)
    card_id = models.CharField(max_length=255, null=True, blank=True)
    vpa = models.CharField(max_length=255, null=True, blank=True)
    fee = models.PositiveIntegerField(null=True, blank=True)
    tax = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = 'payment'
    
class Wallet(models.Model):
    name = models.CharField(max_length=255)
    merchant_id = models.CharField(max_length=255, null=True, blank=True)
    merchant_key = models.CharField(max_length=255, null=True, blank=True)
    industry_type = models.CharField(max_length=255, null=True, blank=True)
    is_active  = models.BooleanField(default=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = "wallet"