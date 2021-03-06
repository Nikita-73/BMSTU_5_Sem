# Generated by Django 3.2.7 on 2021-12-13 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='is_growing',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='price',
        ),
        migrations.AddField(
            model_name='stock',
            name='description',
            field=models.CharField(default=1, max_length=300, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='orcestr',
            field=models.CharField(default=1, max_length=300, verbose_name='Оркестр'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='photo',
            field=models.CharField(default=1, max_length=300, verbose_name='Фото'),
            preserve_default=False,
        ),
    ]
