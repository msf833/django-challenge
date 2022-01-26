from django.db import models
from stadium.models import Stadium
from django.utils import timezone


class Match(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    event_date = models.DateTimeField()
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)
    arbitrator =  models.CharField(max_length=50)
    
    place_of_seats_from_row = models.CharField(max_length=10, null=True)
    place_of_seats_to_row = models.CharField(max_length=10, null=True)
    place_of_seats_from_col = models.CharField(max_length=10, null=True)
    place_of_seats_to_col = models.CharField(max_length=10, null=True)
    
    created_at = models.DateTimeField(default=timezone.now, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.team1} | VS | {self.team2}"

    @classmethod
    def is_reserved(self, reserved_dt):
        reserved_matches = Match.objects.all()
        for match in reserved_matches:
            if match.event_date == reserved_dt:
                return False
        return True
