# Generated by Django 3.1.6 on 2021-02-22 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryv2', '0007_requestbook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestbook',
            name='user',
        ),
        migrations.AddField(
            model_name='requestbook',
            name='yourname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]