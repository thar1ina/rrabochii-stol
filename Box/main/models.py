from django.db import models

class Cloth(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    country = models.CharField(max_length=50)
    description = models.TextField(max_length=500)



    def __str__(self):
        return f'{self.name} {self.country}'