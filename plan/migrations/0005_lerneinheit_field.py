# Generated by Django 5.0.7 on 2024-08-01 11:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0004_alter_lerneinheit_options_alter_thema_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lerneinheit',
            name='field',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='plan.thema', verbose_name='Thema'),
            preserve_default=False,
        ),
    ]
