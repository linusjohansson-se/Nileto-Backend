from .views import ContactPhoneViewSet, ContactViewSet, CustomerViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("contacts", ContactViewSet, basename="contact")
router.register(
    "contact-phones",
    ContactPhoneViewSet,
    basename="contact-phone",
)
router.register("customers", CustomerViewSet, basename="customer")

urlpatterns = []

urlpatterns += router.urls
