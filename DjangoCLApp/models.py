from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=64)
    size = models.IntegerField()
    prize = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name