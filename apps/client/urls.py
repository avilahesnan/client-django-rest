from django.urls import path, include
from rest_framework import routers
from apps.client.views import ClientsViewSet


app_name = 'client'

router = routers.DefaultRouter()

router.register('clients', ClientsViewSet, basename='Clients')

urlpatterns = [
    path('', include(router.urls)),
]
