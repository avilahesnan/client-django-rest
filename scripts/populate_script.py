import os
import django
import random
from faker import Faker
from validate_docbr import CPF
from apps.client.models import Client


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()


def create_peoples(quantity_peoples):
    fake = Faker('en-us')
    Faker.seed(10)
    for _ in range(quantity_peoples):
        cpf = CPF()
        name = fake.name()
        email = '{}@{}'.format(name.lower(), fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()
        rg = "{}{}{}{}".format(random.randrange(10, 99), random.randrange(100, 999), random.randrange(100, 999), random.randrange(0, 9))  # noqa: E501
        phone = "({}) 9{}-{}".format(random.randrange(10, 21), random.randrange(4000, 9999), random.randrange(4000, 9999))  # noqa: E501
        active = random.choice([True, False])
        p = Client(name=name, email=email, cpf=cpf, rg=rg, phone=phone, active=active)  # noqa: E501
        p.save()


create_peoples(5)
