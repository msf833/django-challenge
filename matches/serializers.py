from rest_framework import serializers
from .models import Match

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('stadium' ,'event_date' , 'team1' , 'team2' , 'arbitrator' , 'seat_capacity', 'place_of_seats_from_row', 'place_of_seats_to_row' ,'place_of_seats_from_col' ,
                  'place_of_seats_to_col' ,'created_at' ,'updated_at')

