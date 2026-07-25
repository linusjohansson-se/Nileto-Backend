from rest_framework import viewsets, filters

from .models import Contact
from .serializers import ContactSerializer

class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.prefetch_related("emails", "phone_numbers").order_by("id")
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "emails__email", "phone_numbers__phone_number", "=id"]
