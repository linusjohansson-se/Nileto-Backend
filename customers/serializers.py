from rest_framework import serializers

from .models import Contact, ContactEmail, ContactPhone, Customer

class CustomerSerializer(serializers.ModelSerializer):
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
