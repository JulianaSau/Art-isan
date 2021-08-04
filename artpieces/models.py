from django.db import models

# Create your models here.
class Artist (models.Model):
    artist_name = models.CharField(max_length=250)
    art_type = models.CharField(max_length=500)
    cost = models.BigIntegerField(100)
    art_thumb = models.CharField(max_length=1000)
    
    class Meta:#lets us define the table name in the django db
        db_table = "artist";

    def __str__ (self):
	    return f"{self.artist_name} - {self.art_thumb}"

