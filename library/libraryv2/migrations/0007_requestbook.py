# Generated by Django 3.1.6 on 2021-02-22 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libraryv2', '0006_delete_requestbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('catergory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryv2.bookcatergory')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
