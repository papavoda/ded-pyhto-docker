# Generated by Django 4.1.7 on 2023-05-06 19:02

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiointernal',
            name='tracknumber',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Порядковый номер'),
        ),
        migrations.AlterField(
            model_name='audiointernal',
            name='name',
            field=models.CharField(default='', max_length=250, verbose_name='Название песни'),
        ),
        migrations.AlterField(
            model_name='audiointernal',
            name='track',
            field=models.FileField(upload_to=blog.models.upload_directory, verbose_name='Аудио файл'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, default='', max_length=500, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='intro',
            field=models.TextField(blank=True, default='', help_text='Вступительный текст', max_length=500, null=True, verbose_name='Вступительный текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='keywords',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Ключевые слова'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10, verbose_name='Статус публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=500, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='videoyoutube',
            name='name',
            field=models.CharField(blank=True, default='Видео', max_length=250, null=True, verbose_name='Название видео'),
        ),
    ]
