# Generated by Django 2.1.5 on 2019-01-15 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPosts', '0004_auto_20190115_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Published'),
        ),
    ]