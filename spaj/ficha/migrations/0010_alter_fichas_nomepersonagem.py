# Generated by Django 4.1.1 on 2022-10-06 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0009_alter_fichas_nomepersonagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichas',
            name='nomePersonagem',
            field=models.CharField(default='Pedo', max_length=45),
        ),
    ]