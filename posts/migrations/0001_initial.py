# Generated by Django 4.2.13 on 2024-07-10 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='content')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created_time')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='content')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created_time')),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='post', verbose_name='photo')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post', verbose_name='Post')),
            ],
        ),
    ]
