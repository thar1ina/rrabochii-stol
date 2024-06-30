from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    first_name = models.CharField(max_length=50)
    availability = models.BooleanField(default=True, verbose_name='азыркы учурда иштейт')
    image = models.ImageField(upload_to='p/%Y/%m/%d', blank=True)
    position = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.TextField(max_length=1000, blank=True,verbose_name='Описание')
    website = models.URLField(max_length=200, blank=True, null=True,verbose_name='Ссылка на сайт')

    def __str__(self):
        return f'{self.name} - {self.image}'


class Menu(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Наименование')
    slug = models.CharField(max_length=150, db_index=True, unique=True, verbose_name='Ссылка')
    image = models.ImageField(upload_to='image/%Y/%m/%d', blank=True)
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавление')
    uploaded = models.DateTimeField(auto_now=True, verbose_name='Изменение')

    class Meta:
        ordering = ['name']
        verbose_name = 'menu'
        verbose_name_plural = 'menus'
        index_together = (('id', 'slug'))

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Наименование')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='i/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name


class Restauran(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Наименование')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='im/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name

class Restaura(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Наименование')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='img/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name


class New_dishes(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Цена')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='new_dishes/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name


