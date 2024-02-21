from django.contrib import admin
from apps.client.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cpf', 'active',)
    list_display_links = ('id', 'name', 'cpf',)
    search_fields = ('name', 'cpf',)
    list_filter = ('active',)
    list_editable = ('active',)
    list_per_page = 10
    ordering = ('name',)
