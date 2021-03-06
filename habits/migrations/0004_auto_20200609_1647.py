# Generated by Django 3.0.6 on 2020-06-09 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_auto_20200609_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='goal_quantity',
        ),
        migrations.AlterField(
            model_name='habit',
            name='goal_quantity_unit',
            field=models.CharField(help_text='What unit of measure are you using for your goal? (ex. pages)', max_length=260),
        ),
    ]
