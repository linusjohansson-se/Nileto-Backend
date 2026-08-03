from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from accounts.serializers import CreateUserSerializer, RemoveUserSerializer
from accounts.services import create_user_for_contact, create_user_for_staff, remove_user_for_contact, remove_user_for_staff

class UserViewSet(GenericViewSet):
    
    def get_serializer_class(self):
        if self.action == "create":
            return CreateUserSerializer
        if self.action == "remove":
            return RemoveUserSerializer

    @action(detail=False, methods=["delete"])
    def remove(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        if data.get("staff_id") is not None:
            remove_user_for_staff(data["staff_id"])
        else:
            remove_user_for_contact(data["contact_id"])
        
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        if data.get("staff_id") is not None:
            user_id = create_user_for_staff(email=data["email"], password=data["password"], staff_id=data["staff_id"])
        else:
            user_id = create_user_for_contact(email=data["email"], password=data["password"], contact_id=data["contact_id"])

        return Response({"user_id": user_id}, status=status.HTTP_201_CREATED)
