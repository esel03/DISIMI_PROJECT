# Generated by Django 5.0.7 on 2024-08-09 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neuron', '0002_alter_depend_title_alter_depend_views_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depend',
            name='views_count',
            field=models.BooleanField(default=False),
        ),
    ]
