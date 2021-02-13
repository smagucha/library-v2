# Generated by Django 3.1.6 on 2021-02-13 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
            name='Bookissue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryv2.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryv2.person')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='catergory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryv2.bookcatergory'),
        ),
        migrations.AddField(
            model_name='book',
            name='formatt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryv2.bookformat'),
        ),
    ]
