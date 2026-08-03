

from rest_framework import serializers


class CreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255, write_only=True)
    staff_id = serializers.BigIntegerField(required=False)
    contact_id = serializers.BigIntegerField(required=False)

    def validate(self, attrs):
        has_staff = attrs.get("staff_id") is not None
        has_contact = attrs.get("contact_id") is not None

        if has_staff == has_contact:
            raise serializers.ValidationError("Provide contact OR staff")

        return attrs

class RemoveUserSerializer(serializers.Serializer):
    staff_id = serializers.BigIntegerField(required=False)
    contact_id = serializers.BigIntegerField(required=False)

    def validate(self, attrs):
        has_staff = attrs.get("staff_id") is not None
        has_contact = attrs.get("contact_id") is not None

        if has_staff == has_contact:
            raise serializers.ValidationError("Provide contact OR staff")

        return attrs
