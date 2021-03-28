# Generated by Django 3.1.7 on 2021-03-27 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210328_0054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartprod',
            name='c_type',
        ),
        migrations.AddField(
            model_name='cartprod',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
    ]