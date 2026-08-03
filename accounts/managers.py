from django.contrib.auth.models import BaseUserManager
from allauth.account.models import EmailAddress
from django.db import transaction

class UserManager(BaseUserManager):
    @transaction.atomic
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("An email address is required.")

        if not password:
            raise ValueError("A password must be provided.")

        email = self.normalize_email(email).lower()

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        EmailAddress.objects.create(
                user=user,
                email=user.email,
                primary=True,
                verified=True)

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("is_staff must be set to True for superusers")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("is_superuser must be set to True for superusers")
        
        return self.create_user(email, password, **extra_fields)

