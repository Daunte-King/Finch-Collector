from django.db import models

# Create your models here.


class Finch(models.Model):
    name = models.CharField(max_length=20)
    height = models.CharField(max_length=20)
    vertical = models.IntegerField()

def _str_(self):
    return self.name
