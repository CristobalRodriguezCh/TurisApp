# Generated by Django 3.2 on 2021-11-16 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Maestra', '0003_auto_20211116_1325'),
        ('Trabajador', '0002_alter_trabajador_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajador',
            name='rol',
            field=models.ForeignKey(limit_choices_to={'dependencia': 10}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rol', to='Maestra.maestra'),
        ),
    ]
