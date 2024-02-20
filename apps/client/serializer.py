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
            raise serializers.ValidationError({'cpf': 'The CPF must have 11 digits'})  # noqa: E501
        if not rg_valid(data['rg']):
            raise serializers.ValidationError({'rg': 'ID must be 9 digits long'})  # noqa: E501
        if not phone_valid(data['phone']):
            raise serializers.ValidationError({'phone': 'The mobile phone must have a minimum of 11 digits'})  # noqa: E501
        return data
