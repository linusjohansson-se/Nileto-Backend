from common.views import StandardModelViewSet

from .models import Contact, ContactPhone, Customer, CustomerContact
from .serializers import ContactEmailSerializer, ContactPhoneSerializer, ContactSerializer, CustomerContactSerializer, CustomerSerializer

class ContactViewSet(StandardModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.prefetch_related("emails", "phone_numbers")
    search_fields = ["name", "emails__email", "phone_numbers__phone_number", "=id"]

class ContactPhoneViewSet(StandardModelViewSet):
    serializer_class = ContactPhoneSerializer
    queryset = ContactPhone.objects.all()
    search_fields = ["phone_number", "=id"]

class ContactEmailViewSet(StandardModelViewSet):
    serializer_class = ContactEmailSerializer
    queryset = ContactPhone.objects.all()
    search_fields = ["email", "=id"]

class CustomerViewSet(StandardModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.prefetch_related("addresses")
    search_fields = ["name", "=id"]

class CustomerContactViewSet(StandardModelViewSet):
    serializer_class = CustomerContactSerializer
    queryset = CustomerContact.objects.select_related("customer", "contact")
    search_fields = ["customer_links__name", "contact_links__name", "=id"]
