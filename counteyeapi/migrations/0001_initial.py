# Generated by Django 4.0 on 2022-04-26 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cameras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.TextField()),
                ('descricao', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Cameras',
            },
        ),
    ]
