from rest_framework import serializers
from customers.models import Customer
from customers.validators import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def validate(self, data):
        if not valid_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':"CPF invalid."})
        if not valid_name(data['name']):
            raise serializers.ValidationError({'name':"Do not include numbers in this field."})
        if not valid_phone(data['phone']):
            raise serializers.ValidationError({'phone':"The phone number must follow this pattern: XX XXXXX-XXXX"})
        return data
