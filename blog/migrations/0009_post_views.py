# Generated by Django 4.1.7 on 2023-03-08 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_audiointernal_site_play_alter_post_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.BigIntegerField(blank=True, default=0, null=True, verbose_name='Количество просмотров'),
        ),
    ]
