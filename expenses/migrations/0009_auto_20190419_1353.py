# Generated by Django 2.1.7 on 2019-04-19 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0008_auto_20190419_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]