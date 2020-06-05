# Generated by Django 3.0.6 on 2020-06-05 00:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habit',
            old_name='verb',
            new_name='goal',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='goal_quant',
        ),
        migrations.AddField(
            model_name='dailyrecord',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='habit',
            name='goal_quantity',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='dailyrecord',
            unique_together={('habit', 'recorded_on')},
        ),
    ]
