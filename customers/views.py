from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Customer
from .serializers import CustomerSerializer

@extend_schema(
        request=None,
        responses=CustomerSerializer(many=True),
        tags=["Customer"]
        )
@api_view(["GET"])
def customer_list(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)

    return(Response(serializer.data))

