from django.shortcuts import render
from rest_framework import viewsets

class StandardModelViewSet(viewsets.ModelViewSet):
    filterset_fields = "__all__"
    ordering_fields = "__all__"
    ordering = ["id"]

    class Meta:
        abstract = True
