from rest_framework import serializers
from .models import Contact_Us

class Contact_Us_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Contact_Us
        fields=('__all__')
        