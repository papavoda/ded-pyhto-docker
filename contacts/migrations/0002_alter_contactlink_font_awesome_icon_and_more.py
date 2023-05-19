# Generated by Django 4.1.7 on 2023-02-26 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactlink',
            name='font_awesome_icon',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contactlink',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='icons/contacts/'),
        ),
    ]
