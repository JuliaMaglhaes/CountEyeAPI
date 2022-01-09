# Generated by Django 4.0 on 2022-01-09 01:34

import counteye.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counteye', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='count',
            name='image',
            field=models.ImageField(default='count/default.jpg', upload_to=counteye.models.upload_to, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=110),
        ),
        migrations.AlterField(
            model_name='count',
            name='amount',
            field=models.CharField(max_length=251),
        ),
    ]
