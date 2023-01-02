from rest_framework import serializers
from loja.models import Roupa

class RoupaSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Roupa
        fields = '__all__'
