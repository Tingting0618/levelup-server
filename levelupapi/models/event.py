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
    attendees = models.ManyToManyField(Gamer,related_name='attending')
    
    #joined is a calculated field on the view layer
    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value    