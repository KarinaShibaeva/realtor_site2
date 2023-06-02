# Generated by Django 3.2 on 2023-05-19 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flats', '0002_delete_flat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('price', models.CharField(max_length=128, verbose_name='Цена')),
                ('text', models.TextField(verbose_name='Описание')),
                ('img', models.ImageField(upload_to='%Y/%m/%d/', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Описание')),
                ('location', models.CharField(max_length=128, verbose_name='Расположение')),
            ],
        ),
    ]