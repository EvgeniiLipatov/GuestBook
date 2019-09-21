# Generated by Django 2.2 on 2019-09-21 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='CreatedDate',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='book',
            name='LastEditDate',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата редактирования'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=50, verbose_name='Имя автора'),
        ),
    ]
