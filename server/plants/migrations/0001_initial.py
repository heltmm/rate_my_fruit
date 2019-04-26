# Generated by Django 2.2 on 2019-04-26 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Fruit', 'Fruit'), ('Flower', 'Flower'), ('Vegetable', 'Vegetable')], max_length=9)),
                ('condition', models.CharField(choices=[('Starting', 'Starting'), ('Peak', 'Peak'), ('Ending', 'Ending')], max_length=8)),
                ('name', models.CharField(max_length=100)),
                ('variety', models.CharField(max_length=100)),
                ('location_general', models.CharField(max_length=100)),
                ('location_specific', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
    ]