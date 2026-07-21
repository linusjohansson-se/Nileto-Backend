from django.db import models

from common.models import AuditModel
from django.conf import settings

# Create your models here.

class Employee(AuditModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
            null=False,
            blank=False,
            on_delete=models.RESTRICT)
    name = models.CharField(max_length=100, blank=False, null=False)
