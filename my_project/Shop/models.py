from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='product')
    available = models.BooleanField(default=True, verbose_name='Наличие')


    def __str__(self):
        return f"{self.name} {self.price}"



