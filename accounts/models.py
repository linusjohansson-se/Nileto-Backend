from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.functions import Lower

from accounts.managers import UserManager

class User(AbstractUser):
    username = None # type: ignore[assignment]
    email = models.EmailField(unique=True)
    first_name = None # type: ignore[assignment]
    last_name = None # type: ignore[assignment]

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager() # type: ignore[misc, assignment]

    class Meta(AbstractUser.Meta):
        constraints = [
            models.UniqueConstraint(
                Lower("email"),
                name="accounts_user_email_case_insensitive_unique",)
            ]
