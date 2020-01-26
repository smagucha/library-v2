from django.db import models


# Create your models here.
class Author(models.Model):
    salutation = (
        ('MR', 'Mr'),
        ('MRS', 'Mrs'),
        ('MS', 'Miss'),
    )
    salutation = models.CharField(max_length=4, choices=salutation)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name


class Registerbook(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pages = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    admin_no = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=50)
    #email = models.EmailField()
    #staff_id=models.CharField(max_length=50)
    def __str__(self):
        return self.name
