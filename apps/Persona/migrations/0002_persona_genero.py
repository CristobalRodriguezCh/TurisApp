# Generated by Django 3.2 on 2021-11-16 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Maestra', '0003_auto_20211116_1325'),
        ('Persona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='genero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Maestra.maestra'),
        ),
    ]
