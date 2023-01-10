import re
from validate_docbr import CPF

def valid_cpf(cpf_number):
    cpf = CPF()
    return cpf.validate(cpf_number)

def valid_name(name):
    return name.isalpha()

def valid_phone(phone_number):
    pattern = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    response = re.findall(pattern, phone_number)
    return response