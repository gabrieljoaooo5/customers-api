import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from customers.models import Customer

def populate_customers(amount):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(amount):
        cpf = CPF()
        name = fake.name()
        email = '{}@{}'.format(name.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()
        phone = "{} 9{}-{}".format(random.randrange(10, 21), random.randrange(4000, 9999), random.randrange(4000, 9999))
        active = random.choice([True, False])
        c = Customer(name=name, email=email, cpf=cpf, phone=phone, active=active)
        c.save()

populate_customers(50)
print('Success')