# Generated by Django 5.0.6 on 2024-06-14 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baseproduct',
            options={'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.RemoveField(
            model_name='baseproduct',
            name='external_id',
        ),
    ]
