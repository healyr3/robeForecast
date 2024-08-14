from django.db import models

class RiverData(models.Model):
    riverID = models.IntegerField()
    riverName = models.CharField(max_length=100)
    datetime = models.DateField()
    stage = models.FloatField()

    def __str__(self):
        return f'{self.riverName} - {self.datetime} - {self.stage}'
