from rest_framework import serializers
from apps.client.models import Client
from apps.client.validators import (
    name_valid,
    cpf_valid,
    rg_valid,
    phone_valid
)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ['created_at', 'updated_at']

    def validate(self, data):
        if not name_valid(data['name']):
            raise serializers.ValidationError({'name': 'The name cannot include numbers'})  # noqa: E501
        if not cpf_valid(data['cpf']):
            raise serializers.ValidationError({'cpf': 'The CPF is invalid'})
        if not rg_valid(data['rg']):
            raise serializers.ValidationError({'rg': 'The ID is invalid'})
        if not phone_valid(data['phone']):
            raise serializers.ValidationError({'phone': 'This mobile phone format is not supported'})  # noqa: E501
        return data
