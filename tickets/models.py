from django.db import models
from django.db import models
from stadium.models import Stadium
from matches.models import Match
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Ticket(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    def __str__(self):
        return f"Ticket | location {self.match} |owner {self.owner}"

    def get_absolute_url(self):
        return reverse("Ticket_detail", kwargs={"pk": self.pk})
