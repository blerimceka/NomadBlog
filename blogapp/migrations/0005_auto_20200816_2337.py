# Generated by Django 2.2.7 on 2020-08-16 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_auto_20200816_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
