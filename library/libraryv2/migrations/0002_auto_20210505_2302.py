# Generated by Django 3.1.6 on 2021-05-05 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libraryv2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.PositiveIntegerField()),
                ('studentid', models.CharField(max_length=200, unique=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='bookissue',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryv2.student'),
        ),
        migrations.AlterField(
            model_name='requestbook',
            name='yourname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryv2.student'),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
