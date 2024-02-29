from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from apps.client.serializer import ClientSerializer
from apps.client.models import Client


class ClientsViewSet(viewsets.ModelViewSet):
    '''
    View all clients.

    Returns:
        List of all clients.
    '''

    queryset = Client.objects.all().order_by('name')
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]  # noqa: E501
    ordering_fields = ['name']
    search_fields = ['name', 'cpf']
    filterset_fields = ['active']

    @method_decorator(cache_page(30))
    def dispatch(self, *args, **kwargs):
        return super(ClientsViewSet, self).dispatch(*args, **kwargs)
