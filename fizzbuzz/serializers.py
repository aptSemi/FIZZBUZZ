from rest_framework import serializers
from .models import Fizzbuzz

class FizzbuzzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fizzbuzz 
        fields = ['id', 'name', 'description']
