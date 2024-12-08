from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.title} duration: {self.duration} min"
