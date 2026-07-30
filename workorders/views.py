from common.views import StandardModelViewSet
from workorders.models import Action, ActionType, WorkOrder, WorkOrderPriority, WorkOrderStatus, WorkOrderType
from workorders.serializers import ActionSerializer, ActionTypeSerializer, WorkOrderPrioritySerializer, WorkOrderSerializer, WorkOrderStatusSerializer, WorkOrderTypeSerializer

class WorkOrderViewSet(StandardModelViewSet):
    serializer_class = WorkOrderSerializer
    queryset = WorkOrder.objects.select_related(
        "customer",
        "contact",
        "status",
        "priority",
        "type",
    ).prefetch_related(
        "customer__addresses",
        "contact__emails",
        "contact__phone_numbers",
    )    
    search_fields = ["=id", "customer__name", "description", "contact__name"]

class WorkOrderStatusViewSet(StandardModelViewSet):
    serializer_class = WorkOrderStatusSerializer
    queryset = WorkOrderStatus.objects.all()
    search_fields = ["=id", "name"]

class WorkOrderPriorityViewSet(StandardModelViewSet):
    serializer_class = WorkOrderPrioritySerializer
    queryset = WorkOrderPriority.objects.all()
    search_fields = ["=id", "name"]

class WorkOrderTypeViewSet(StandardModelViewSet):
    serializer_class = WorkOrderTypeSerializer
    queryset = WorkOrderType.objects.all()
    search_fields = ["=id", "name"]

class ActionViewSet(StandardModelViewSet):
    serializer_class = ActionSerializer
    queryset = Action.objects.select_related("type")

class ActionTypeViewSet(StandardModelViewSet):
    serializer_class = ActionTypeSerializer
    queryset = ActionType.objects.all()
    search_fields = ["=id", "name"]


