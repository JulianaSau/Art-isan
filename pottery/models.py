from django.db import models

# Create your models here.
class pottery(models.Model):
    artist_name = models.CharField(max_length=250)
    genre = models.CharField(max_length=500)
    cost = models.BigIntegerField(100)
    art_thumb = models.CharField(max_length=1000)

    def __str__ (self):
	    return f"{self.artist_name} - {self.art_thumb}"