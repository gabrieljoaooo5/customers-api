from rest_framework import serializers
from customers.models import Customer
from customers.validators import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def validate(self, data):
        if not valid_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':"The CPF must have 11 digits."})
        if not valid_name(data['name']):
            raise serializers.ValidationError({'name':"Do not include numbers in this field."})
        return data
