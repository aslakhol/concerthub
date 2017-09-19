from django.db import models

# Create your models here.

class Stage(models.Model):
    name = models.CharField(max_length=120)
    capacity = models.IntegerField()
    def __str__(self):
        return self.name


class Concert(models.Model):
    artist = models.CharField(max_length=120)
    stage = models.ForeignKey(Stage)
    date = models.DateField(null=True, blank=True)
    spectator_amount = models.IntegerField()
    def __str__(self):
        return self.artist

