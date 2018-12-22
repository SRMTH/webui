# Generated by Django 2.1.4 on 2018-12-13 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motor',
            name='current_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='motor',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='motor',
            name='pyplot_support',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='motor',
            name='sdk_support',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='motor',
            name='wizard_support',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
