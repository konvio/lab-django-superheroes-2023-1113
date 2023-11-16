# Generated by Django 4.2.7 on 2023-11-16 18:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("heroes", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="hero",
            name="power",
        ),
        migrations.AddField(
            model_name="hero",
            name="alias",
            field=models.CharField(default="Hero", max_length=40),
        ),
        migrations.AddField(
            model_name="hero",
            name="description",
            field=models.TextField(default="Brave Hero", max_length=400),
        ),
        migrations.AddField(
            model_name="hero",
            name="intelligence",
            field=models.PositiveSmallIntegerField(
                default=0, validators=[django.core.validators.MaxValueValidator(10)]
            ),
        ),
        migrations.AddField(
            model_name="hero",
            name="lost_battles",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="hero",
            name="magic",
            field=models.PositiveSmallIntegerField(
                default=0, validators=[django.core.validators.MaxValueValidator(10)]
            ),
        ),
        migrations.AddField(
            model_name="hero",
            name="public_recognition",
            field=models.PositiveSmallIntegerField(
                default=0, validators=[django.core.validators.MaxValueValidator(100)]
            ),
        ),
        migrations.AddField(
            model_name="hero",
            name="strength",
            field=models.PositiveSmallIntegerField(
                default=0, validators=[django.core.validators.MaxValueValidator(10)]
            ),
        ),
        migrations.AddField(
            model_name="hero",
            name="won_battles",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="hero",
            name="name",
            field=models.CharField(default="Alice Brown", max_length=40),
        ),
    ]