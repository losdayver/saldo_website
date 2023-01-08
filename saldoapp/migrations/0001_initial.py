# Generated by Django 4.0.4 on 2023-01-07 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InitialSaldo',
            fields=[
                ('apartment_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('value', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField()),
                ('month', models.PositiveIntegerField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=7)),
                ('saldo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saldoapp.initialsaldo')),
            ],
            options={
                'unique_together': {('saldo_id', 'year', 'month')},
            },
        ),
    ]
