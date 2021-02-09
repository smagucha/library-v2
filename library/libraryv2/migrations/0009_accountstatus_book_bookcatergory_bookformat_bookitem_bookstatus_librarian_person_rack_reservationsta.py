# Generated by Django 3.1.5 on 2021-02-09 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libraryv2', '0008_auto_20210209_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statusaccount', models.CharField(choices=[('Active', 'Active'), ('closed', 'closed'), ('Canceled', 'Canceled'), ('Blacklisted', 'Blacklisted'), ('Nill', 'Nill')], default='Nill', max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=200)),
                ('nobooks', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BookCatergory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BookFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bookformat', models.CharField(choices=[('HARDCOVER', 'HARDCOVER'), ('PAPERBACK', 'PAPERBACK'), ('NEWSPAPER', 'NEWSPAPER'), ('MAGAZINE', 'MAGAZINE'), ('JOURNAL', 'JOURNAL')], default='HARDCOVER', max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='BookStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookstatus', models.CharField(choices=[('AVAILABLE', 'AVAILABLE'), ('RESERVED', 'RESERVED'), ('LOANED', 'LOANED'), ('LOST', 'LOST')], default='AVAILABLE', max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveIntegerField()),
                ('librarianid', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveIntegerField()),
                ('studentid', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_identifier', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ReservationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resstatus', models.CharField(choices=[('WAITING', 'WAITING'), ('CANCELED', 'CANCELED'), ('NONE', 'NONE')], default='NONE', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='BookItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed', models.BooleanField(default=False)),
                ('due_date', models.DateField()),
                ('price', models.PositiveIntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryv2.book')),
                ('book_format', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryv2.bookstatus')),
                ('rack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryv2.rack')),
            ],
        ),
    ]