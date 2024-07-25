# Generated by Django 5.0.7 on 2024-07-24 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('barcode', models.ImageField(blank=True, upload_to='barcodes/', verbose_name='Штрих код')),
                ('date_last_invent', models.DateTimeField(blank=True, null=True, verbose_name='Дата последней инвентаризации')),
                ('date_last_check', models.DateTimeField(blank=True, null=True, verbose_name='Дата последней проверки')),
                ('image', models.ImageField(blank=True, null=True, upload_to='equipment_images/', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]
