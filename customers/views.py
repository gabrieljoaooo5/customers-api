from rest_framework import viewsets
from customers.serializers import CustomerSerializer
from customers.models import Customer

class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

