import uuid

from django.conf import settings
from django.db import models
from simple_history.models import HistoricalRecords

class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class AuditModel(BaseModel):
    history = HistoricalRecords(inherit=True)

    class Meta(BaseModel.Meta):
        abstract = True
