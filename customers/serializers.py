from rest_framework import fields, serializers

from .models import Contact, ContactEmail, ContactPhone, Customer, CustomerAddress

class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = "__all__"

class CustomerSerializer(serializers.ModelSerializer):
    addresses = CustomerAddressSerializer(many = True)

    class Meta:
        model = Customer
        fields = "__all__"

class ContactPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPhone
        fields = "__all__"

class ContactEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactEmail
        fields = "__all__"

class ContactSerializer(serializers.ModelSerializer):
    phone_numbers = ContactPhoneSerializer(many=True, read_only=True)
    emails = ContactEmailSerializer(many=True, read_only=True)

    class Meta:
        model = Contact
        fields = "__all__"
