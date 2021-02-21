from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

class Person(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
	phone =models.PositiveIntegerField()
	studentid = models.CharField(max_length= 200)

	# def __str__(self):
	# 	return self.user

class Librarian(models.Model):
	user = models.OneToOneField(User, models.CASCADE,  null = True)
	phone =models.PositiveIntegerField()
	librarianid = models.CharField(max_length= 200)

class BookFormat(models.Model):
	HARDCOVER='HARDCOVER'
	PAPERBACK= 'PAPERBACK'
	NEWSPAPER='NEWSPAPER'
	MAGAZINE= 'MAGAZINE'
	JOURNAL='JOURNAL'
	
	book =(
		(HARDCOVER, 'HARDCOVER'),
  		(PAPERBACK, 'PAPERBACK'),
  		(NEWSPAPER,'NEWSPAPER'),
  		(MAGAZINE, 'MAGAZINE'),
  		(JOURNAL, 'JOURNAL'),
	)
	Bookformat = models.CharField(
		max_length=9,
		choices=book,
		default=HARDCOVER,
    )

class BookCatergory(models.Model):
	name= models.CharField(max_length= 200)

	def __str__(self):
 		return self.name

class Book(models.Model):
	title = models.CharField(max_length = 200)
	subject = models.CharField(max_length= 200)
	publisher = models.CharField(max_length= 200)
	authors = models.CharField(max_length= 200)
	nobooks = models.PositiveIntegerField()
	catergory =models.ForeignKey(BookCatergory, on_delete= models.CASCADE)
	formatt = models.ForeignKey(BookFormat, on_delete= models.CASCADE)
	def __str__(self):
 		return self.title

class Bookissue(models.Model):
	student= models.ForeignKey(Person, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete = models.CASCADE)
	given_date =models.DateTimeField(auto_now_add = True, auto_now= False)
	due_date = models.DateField()

class RequestBook(models.Model):
	title = models.CharField(max_length = 200)
	catergory = models.ForeignKey(BookCatergory, on_delete=models.CASCADE)




 	
  	
 
