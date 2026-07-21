from django.db import models
from django.db.models.deletion import RESTRICT

from common.models import AuditModel, BaseModel

from customers.models import Customer
from users.models :

class OrderType(BaseModel):
    name = models.CharField(max_length=255)

class WorkOrder(AuditModel):
    description = models.CharField(max_length=255)
    customer_id = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT, null=True)
    type = models.ForeignKey(OrderType, on_delete=models.RESTRICT)



