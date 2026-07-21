from django.db import models

from common.models import AuditModel

class Employee(AuditModel):
    name = models.CharField(max_length=100, null=False, blank=False)   
