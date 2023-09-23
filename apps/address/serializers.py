from rest_framework import serializers

from public.models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id', 
            'created',
            'updated',
            'street', 
            'city', 
            'postal_code',
            'province',
            'country'
        )