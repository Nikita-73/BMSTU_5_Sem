from django.db import models


class Stock(models.Model):
    id_d = models.CharField(max_length=40, verbose_name="idd")
    src = models.CharField(max_length=300, verbose_name="Фото")
    title = models.CharField(max_length=300, verbose_name="Оркестр")
    text = models.CharField(max_length=300, verbose_name="Описание")

