from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, unique=True)
    nickname = models.CharField(max_length=50, blank=True)
    loyalty_points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name