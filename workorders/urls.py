from rest_framework.routers import DefaultRouter

from workorders.views import ActionTypeViewSet, ActionViewSet, WorkOrderPriorityViewSet, WorkOrderStatusViewSet, WorkOrderTypeViewSet, WorkOrderViewSet


router = DefaultRouter()

router.register("workorder", WorkOrderViewSet, basename="workorder")
router.register("workorder-status", WorkOrderStatusViewSet, basename="workorder-status")
router.register("workorder-type", WorkOrderTypeViewSet, basename="workorder-type")
router.register("workorder-priority", WorkOrderPriorityViewSet, basename="workorder-priority")
router.register("action", ActionViewSet, basename="action")
router.register("action-type", ActionTypeViewSet, basename="action-type")

urlpatterns = router.urls
