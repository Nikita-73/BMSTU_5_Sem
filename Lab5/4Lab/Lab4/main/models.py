from django.db import models


class IceCream(models.Model):
    title = models.CharField('Название', max_length=50)
    abouticecr = models.TextField('Цена')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Мороженное'
        verbose_name_plural = 'Мороженное'

