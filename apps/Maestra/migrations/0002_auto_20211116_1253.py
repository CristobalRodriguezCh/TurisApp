# Generated by Django 3.2 on 2021-11-16 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maestra', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maestra',
            name='dependencia',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='maestra',
            name='valor',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
