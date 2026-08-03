from django.db import models

from common.models import AuditModel
from django.conf import settings

class Staff(AuditModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
            null=False,
            blank=False,
            on_delete=models.RESTRICT,
            related_name="staff")
    name = models.CharField(max_length=100, blank=False, null=False)
