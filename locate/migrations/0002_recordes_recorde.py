# Generated by Django 3.0.1 on 2020-01-31 14:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('locate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordes',
            name='recorde',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]