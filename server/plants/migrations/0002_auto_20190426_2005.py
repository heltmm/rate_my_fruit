# Generated by Django 2.2 on 2019-04-26 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='plant',
            name='location_specific',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='plant',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='plant',
            name='variety',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
