from rest_framework import viewsets
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
