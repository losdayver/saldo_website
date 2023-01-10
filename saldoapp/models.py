from django.db import models

# Create your models here.

class InitialSaldo(models.Model):
    class Meta:
        unique_together = ('apartment_id', 'year')

    apartment_id = models.PositiveIntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.PositiveIntegerField()

class Payment(models.Model):
    class Meta:
        unique_together = ('apartment_id', 'year', 'month')

    apartment_id = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()

    value = models.DecimalField(max_digits=10, decimal_places=2)

class Charge(models.Model):
    class Meta:
        unique_together = ('apartment_id', 'year', 'month')

    apartment_id = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()

    value = models.DecimalField(max_digits=10, decimal_places=2)