from rest_framework import viewsets, filters
from customers.serializers import CustomerSerializer
from customers.models import Customer
from django_filters.rest_framework import DjangoFilterBackend

class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'cpf']
    filterset_fields = ['active']

