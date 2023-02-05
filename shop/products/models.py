from django.db import models

class Category(models.Model):
    '''Категории'''
    name = models.CharField(verbose_name='Категория', max_length=150)
    url = models.SlugField(max_length=160, unique=True)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    '''Товары'''
    SIZE_CHOICES = [
        ('Sneakers', (
            ('7', '7'),
            ('7.5', '7.5'),
            ('8', '8'),
            ('8.5', '8.5'),
            ('9', '9'),
            ('10', '10'),
            ('10.5', '10.5'),
            ('11', '11'),
            ('11.5', '11.5'),
            ('12', '12'),
            ('12.5', '12.5'),
        )),
        ('Clothes', (
            ('S', 'Size S'),
            ('M', 'Size M'),
            ('L', 'Size L'),
            ('XL', 'Size XL'),
            ('XXL', 'Size XXL'),
        ))
    ]
    image = models.ImageField(verbose_name='Изображение')
    name = models.CharField(max_length=50, verbose_name='Название')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    color = models.CharField(max_length=20, verbose_name='Цвет')
    size = models.CharField(max_length=50, choices=SIZE_CHOICES, verbose_name='Размер')
    description = models.TextField(verbose_name='Описание')
    ingredients = models.CharField(max_length=200, verbose_name='Состав')
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField(verbose_name='Черновик', default=False)

    category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'



