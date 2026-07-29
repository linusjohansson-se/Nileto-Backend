
from .views import ContactEmailViewSet, ContactPhoneViewSet, ContactViewSet, CustomerContactViewSet, CustomerViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("contacts", ContactViewSet, basename="contact")
router.register(
    "contact-phones",
    ContactPhoneViewSet,
    basename="contact-phone",
)
router.register("customers", CustomerViewSet, basename="customer")
router.register("contact-email", ContactEmailViewSet, basename="contact-email")
router.register("customer-contact", CustomerContactViewSet, basename="customer-contact")
urlpatterns = []

urlpatterns += router.urls
