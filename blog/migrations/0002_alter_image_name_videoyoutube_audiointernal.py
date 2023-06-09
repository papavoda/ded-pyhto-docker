# Generated by Django 4.1.7 on 2023-02-26 10:51

import blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.CreateModel(
            name='VideoYoutube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('video_frame', models.CharField(max_length=900)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='videos_youtube', to='blog.post')),
            ],
        ),
        migrations.CreateModel(
            name='AudioInternal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('track', models.FileField(upload_to=blog.models.upload_directory)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audio_internal', to='blog.post')),
            ],
        ),
    ]
