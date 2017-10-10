from django.db import models

__all__ = (
    'Manufacturer',
    'Car',
    'User',
)

class Manufacturer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'제조사: {self.name}'


class Car(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'''모델명: {self.name}
         제조사: {self.manufacturer.name}'''


class User(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
