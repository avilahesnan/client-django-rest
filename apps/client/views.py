from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.client.serializer import ClientSerializer
from apps.client.models import Client


class ClientsViewSet(viewsets.ModelViewSet):
    '''
    View all clients.

    Returns:
        List of all clients.
    '''

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]  # noqa: E501
    ordering_fields = ['name']
    search_fields = ['name', 'cpf']
    filterset_fields = ['active']
