# Generated by Django 4.0.4 on 2023-01-10 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment_id', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
                ('month', models.PositiveIntegerField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'unique_together': {('apartment_id', 'year', 'month')},
            },
        ),
        migrations.CreateModel(
            name='InitialSaldo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment_id', models.PositiveIntegerField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('year', models.PositiveIntegerField()),
            ],
            options={
                'unique_together': {('apartment_id', 'year')},
            },
        ),
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment_id', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
                ('month', models.PositiveIntegerField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'unique_together': {('apartment_id', 'year', 'month')},
            },
        ),
    ]