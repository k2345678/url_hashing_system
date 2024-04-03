from django.db import models

class URL(models.Model):
    original_url = models.URLField(unique=True)
    hashed_url = models.CharField(max_length=100, unique=True)
    clicks = models.IntegerField(default=0)

