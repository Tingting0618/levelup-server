from django.db import models
from levelupapi.models.game import Game
from levelupapi.models.gamer import Gamer


class Event(models.Model):
    game = models.ForeignKey(
        Game, verbose_name="organizer", on_delete=models.SET_NULL, null=True)
    organizer = models.ForeignKey(
        Gamer, verbose_name="organizer", on_delete=models.SET_NULL, null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    description = models.CharField(max_length=50)