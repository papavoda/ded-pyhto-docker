# Generated by Django 4.1.7 on 2023-03-04 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_image_name_alter_post_intro_alter_post_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='intro',
            field=models.TextField(blank=True, default='', help_text='Little intro text', max_length=500, null=True, verbose_name='Вступительный текст'),
        ),
    ]