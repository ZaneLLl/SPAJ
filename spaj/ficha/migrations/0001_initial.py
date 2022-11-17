# Generated by Django 4.1.1 on 2022-10-06 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fichas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomePersonagem', models.CharField(max_length=45)),
                ('historiaPersonagem', models.TextField(max_length=1000)),
                ('LVL', models.CharField(max_length=2)),
                ('SAB', models.CharField(max_length=2)),
                ('AGL', models.CharField(max_length=2)),
                ('CON', models.CharField(max_length=2)),
                ('DES', models.CharField(max_length=2)),
                ('CTF', models.CharField(max_length=2)),
                ('PER', models.CharField(max_length=2)),
                ('CAR', models.CharField(max_length=2)),
                ('VIT', models.CharField(max_length=2)),
                ('FOR', models.CharField(max_length=2)),
                ('LUT', models.CharField(max_length=2)),
            ],
        ),
    ]