from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('match' ,'owner' , 'created_at' , 'updated_at' )

