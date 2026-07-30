

from rest_framework import serializers

from customers.serializers import ContactSerializer, CustomerSerializer
from workorders.models import Action, ActionType, WorkOrder, WorkOrderPriority, WorkOrderStatus, WorkOrderType

class WorkOrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrderStatus
        fields = "__all__"

class WorkOrderPrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrderPriority
        fields = "__all__"

class WorkOrderTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrderType
        fields = "__all__"

class WorkOrderSerializer(serializers.ModelSerializer):
    priority = WorkOrderPrioritySerializer(read_only=True)
    status = WorkOrderStatusSerializer(read_only=True)
    type = WorkOrderTypeSerializer(read_only=True)
    contact = ContactSerializer(read_only=True)
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = WorkOrder
        fields = "__all__"

class ActionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionType
        fields = "__all__"

class ActionSerializer(serializers.ModelSerializer):
    type = ActionTypeSerializer(read_only=True)

    class Meta:
        model = Action
        fields = "__all__"

