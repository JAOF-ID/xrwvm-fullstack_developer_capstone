
from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# CAR MAKE CLASS
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation

CAR_TYPES = [
    ('SEDAN', 'Sedan'),
    ('SUV', 'SUV'),
    ('WAGON', 'Wagon'),
    ('Cabriolet', 'Cabriolet'),
    ('Roadster', 'Roadster'),
    ('Sport car', 'Sport car'),
    ]

ENGINE_FUEL_TYPE = [
    ('GASOLINE', 'Gasoline'),
    ('DIESEL', 'Diesel'),
    ('HYBRID', 'Hybrid'),
    ('HYBRID-PLUGIN', 'Hybrid plug-in'),
    ('FULL-ELECTRIC', 'Full Electric'),
    ]

# CAR MODEL CLASS
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2024,
        validators=[
            MaxValueValidator(2024),
            MinValueValidator(2015)
        ])
    engine_type = models.CharField(max_length=15, choices=ENGINE_FUEL_TYPE, default='GASOLINE')
    kilometers = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(9999999),
            MinValueValidator(0)
        ])


    def __str__(self):
        return self.name  # Return the name as the string representation


