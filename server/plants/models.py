from django.db import models

class Plant(models.Model):
    TYPES               = (
        ('Fruit', 'Fruit'),
        ('Flower', 'Flower'),
        ('Vegetable', 'Vegetable')
    )
    CONDITIONS               = (
        ('Starting', 'Starting'),
        ('Peak', 'Peak'),
        ('Ending', 'Ending')
    )
    type                = models.CharField(max_length=9, choices=TYPES)
    condition           = models.CharField(max_length=8, choices=CONDITIONS)
    name                = models.CharField(max_length=100)
    variety             = models.CharField(max_length=100, blank=True)
    location_general    = models.CharField(max_length=100)
    location_specific   = models.CharField(max_length=100, blank=True)
    latitude            = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    longitude           = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    date                = models.DateField()
    description         = models.TextField(blank=True)
