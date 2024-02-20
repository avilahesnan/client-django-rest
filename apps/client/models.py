from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    email = models.EmailField(max_length=40, null=False, blank=False)
    cpf = models.CharField(max_length=14, unique=True, null=False, blank=False)
    rg = models.CharField(max_length=9, null=False, blank=False)
    phone = models.CharField(max_length=15)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'
