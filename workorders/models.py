import re

from django.db import models

from business.models import Employee
from common.models import AuditModel

from customers.models import Contact, Customer

class WorkOrderType(AuditModel):
    name = models.CharField(max_length=100, null=False, blank=False)

class WorkOrderStatus(AuditModel):
    name = models.CharField(max_length=100, null=False, blank=False)

class WorkOrderPriority(AuditModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    severity = models.IntegerField(blank=False, null=False, default=0)

class WorkOrder(AuditModel):
    description = models.CharField(max_length=255, null=False, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, related_name="work_orders", null=False)
    contact = models.ForeignKey(Contact, on_delete=models.RESTRICT, related_name="work_orders", null=True)
    type = models.ForeignKey(WorkOrderType, on_delete=models.RESTRICT, related_name="work_orders", null=False)
    status = models.ForeignKey(WorkOrderStatus, on_delete=models.RESTRICT, related_name="work_orders", null=False)
    priority = models.ForeignKey(WorkOrderPriority, on_delete=models.RESTRICT, related_name="work_orders", null=False)

class ActionType(AuditModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    billable = models.BooleanField(null=False, default=False)
    price = models.DecimalField(null=True, max_digits=12, decimal_places=2)
    cost = models.DecimalField(null=True, max_digits=12, decimal_places=2)
    export_id = models.CharField(null=False, blank=True, default="")
    time_tracking = models.BooleanField(null=False, default=False)

class Action(AuditModel):
    employee = models.ForeignKey(Employee, on_delete=models.RESTRICT, null=False, related_name="actions")
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, null=False, related_name="actions")
    action_type = models.ForeignKey(ActionType, on_delete=models.RESTRICT)
    note = models.TextField(null=False, blank=True)
    internal_note = models.TextField(null=False, blank=True)
    start_time = models.DateTimeField(null=True)
    time_taken = models.DurationField(null=True)
    invoiced = models.BooleanField(null=False)


