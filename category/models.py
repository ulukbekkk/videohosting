from django.db import models

class Genre(models.Model):
    slug = models.SlugField(max_length=10)
    genre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.genre