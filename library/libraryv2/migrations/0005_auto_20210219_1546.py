# Generated by Django 3.1.6 on 2021-02-19 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryv2', '0004_auto_20210219_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='librarian',
            name='email',
        ),
        migrations.RemoveField(
            model_name='librarian',
            name='name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='email',
        ),
        migrations.RemoveField(
            model_name='person',
            name='name',
        ),
    ]