from django.db import models
from levelupapi.models.gamer import Gamer
from levelupapi.models.gametype import GameType


class Game(models.Model):
    title = models.CharField(max_length=50,null=True)
    maker = models.CharField(max_length=50,null=True)
    game_type = models.ForeignKey(GameType, on_delete=models.SET_NULL, null=True)
    number_of_players = models.IntegerField(null=True)
    gamer = models.ForeignKey(Gamer,on_delete=models.SET_NULL, null=True, related_name='games')
    skill_level = models.IntegerField(null=True)
#https://stackoverflow.com/questions/44160983/what-does-related-name-do/44161722#44161722