from rest_framework import viewsets, filters

from .models import Contact, ContactPhone, Customer
from .serializers import ContactPhoneSerializer, ContactSerializer, CustomerSerializer

class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.prefetch_related("emails", "phone_numbers")
    search_fields = ["name", "emails__email", "phone_numbers__phone_number", "=id"]
    filterset_fields = "__all__"
    ordering_fields = "__all__"
    ordering = ["id"]

class ContactPhoneViewSet(viewsets.ModelViewSet):
    serializer_class = ContactPhoneSerializer
    queryset = ContactPhone.objects.all()
    search_fields = ["phone_number", "=id"]
    filterset_fields = "__all__"
    ordering_fields = "__all__"
    ordering = ["id"]

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.prefetch_related("addresses")
    search_fields = ["name", "=id"]
    filterset_fields = "__all__"
    ordering_fields = "__all__"
    ordering = ["id"]
