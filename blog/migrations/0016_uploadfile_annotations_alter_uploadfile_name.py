# Generated by Django 4.1.7 on 2023-05-19 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_uploadfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='annotations',
            field=models.CharField(default='Скачать весь альбом', max_length=255, verbose_name='Скачать целиком итп'),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Имя файла'),
        ),
    ]