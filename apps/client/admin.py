from django.contrib import admin
from apps.client.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('active',)
    list_editable = ('active',)
    list_per_page = 10
