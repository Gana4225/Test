from rest_framework import serializers
from .models import pdata

class sec(serializers.ModelSerializer):
    class Meta:
        model= pdata
        fields='__all__'