# Generated by Django 3.1.6 on 2021-05-15 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryv2', '0003_auto_20210505_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='user',
            field=models.CharField(choices=[('A', 'Student')], max_length=1),
        ),
    ]
