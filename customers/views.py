from rest_framework import viewsets, filters

from common.views import StandardModelViewSet

from .models import Contact, ContactPhone, Customer
from .serializers import ContactPhoneSerializer, ContactSerializer, CustomerSerializer

class ContactViewSet(StandardModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.prefetch_related("emails", "phone_numbers")
    search_fields = ["name", "emails__email", "phone_numbers__phone_number", "=id"]

class ContactPhoneViewSet(StandardModelViewSet):
    serializer_class = ContactPhoneSerializer
    queryset = ContactPhone.objects.all()
    search_fields = ["phone_number", "=id"]

class CustomerViewSet(StandardModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.prefetch_related("addresses")
    search_fields = ["name", "=id"]
