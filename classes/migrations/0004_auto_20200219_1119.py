# Generated by Django 2.1.5 on 2020-02-19 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_auto_20200219_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=8),
        ),
    ]
