from rest_framework import serializers
from .models import Stadium

class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = ('name' ,'founded_in' , 'capacity' , 'address' , 'city' , 'created_at' ,'updated_at')

    