from django.db import models



class Orders(models.Model):
    
    order_id = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    amount_paid = models.PositiveIntegerField()
    amount_due = models.PositiveIntegerField()
    currency = models.CharField(max_length=10)
    receipt = models.CharField(max_length=255, null=True, blank=True)
    offer_id = models.PositiveIntegerField(null=True, blank=True)
    status = models.PositiveIntegerField(null=True, blank=True)
    attempts = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.PositiveIntegerField()
    updated_at = models.PositiveIntegerField()
    
    class Meta:
        db_table = "orders"
        
        
class OrderNoteMapping(models.Model):
    
    order_pk = models.PositiveIntegerField()
    note_description = models.TextField(null=True, blank=True)
    created_at = models.PositiveIntegerField()
    updated_at = models.PositiveIntegerField()
