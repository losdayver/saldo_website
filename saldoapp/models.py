from django.db import models

# Create your models here.

class InitialSaldo(models.Model):
    apartment_id = models.PositiveIntegerField(primary_key=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.PositiveIntegerField()

class Payment(models.Model):
    class Meta:
        unique_together = ('saldo_id', 'year', 'month')

    saldo_id = models.ForeignKey(InitialSaldo, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()

    value = models.DecimalField(max_digits=10, decimal_places=2)

class Charge(models.Model):
    class Meta:
        unique_together = ('saldo_id', 'year', 'month')

    saldo_id = models.ForeignKey(InitialSaldo, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()

    value = models.DecimalField(max_digits=10, decimal_places=2)