from django.db import models


class Music(models.Model):
    song = models.TextField(default="song")
    singer = models.TextField(default='AKB48')
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Mate:
        db_table = "music"
