from django.utils import timezone
from django.db import models



class Orders(models.Model):
    
    CREATED = 0
    ATTEMPTED = 1
    PAID =2
    
    STATUS_CHOICE =(
        (CREATED, "Created"),
        (ATTEMPTED, "Attempted"),
        (PAID, "Paid"),
    ) 
    
    order_id = models.CharField(max_length=255)
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
