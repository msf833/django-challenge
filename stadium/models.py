from django.db import models
from django.utils import timezone

# Create your models here.


class Stadium(models.Model):
    name = models.CharField(max_length=150)
    founded_in = models.DateTimeField(editable=True )
    capacity = models.IntegerField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)

    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f"Name : {self.name} | City :{self.city}  | Founded : {self.founded_in} | Capacity : {self.capacity} "

    class Meta:
        db_table = 'stadiums'
        managed = True
        verbose_name = 'Stadium'
        verbose_name_plural = 'Stadiums'
