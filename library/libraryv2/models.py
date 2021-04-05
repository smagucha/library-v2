from django.conf import settings
from django.contrib.auth import get_user_model as user_model
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

User = user_model()

class Person(models.Model):
	#user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True)
	phone =models.PositiveIntegerField()
	studentid = models.CharField(max_length= 200)

	def __str__(self):
		return str(self.user)

class Librarian(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE,  null = True)
	phone =models.PositiveIntegerField()
	librarianid = models.CharField(max_length= 200)

	def __str__(self):
		return str(self.user)



class BookCatergory(models.Model):
	name= models.CharField(max_length= 200)

	def __str__(self):
 		return self.name

	class Meta:
		verbose_name_plural = "BookCategories"


class Book(models.Model):
	HARDCOVER='HARDCOVER'
	PAPERBACK= 'PAPERBACK'
	NEWSPAPER='NEWSPAPER'
	MAGAZINE= 'MAGAZINE'
	JOURNAL='JOURNAL'
	
	bookf =(
		(HARDCOVER, 'HARDCOVER'),
  		(PAPERBACK, 'PAPERBACK'),
  		(NEWSPAPER,'NEWSPAPER'),
  		(MAGAZINE, 'MAGAZINE'),
  		(JOURNAL, 'JOURNAL'),
	)
	title = models.CharField(max_length = 200)
	subject = models.CharField(max_length= 200)
	publisher = models.CharField(max_length= 200)
	authors = models.CharField(max_length= 200)
	availablebook = models.PositiveIntegerField()
	givenout=models.PositiveIntegerField(default=0, null= True)
	catergory =models.ForeignKey(BookCatergory, on_delete= models.CASCADE)
	Bookformat = models.CharField(
		max_length=9,
		choices=bookf,
		default=HARDCOVER,
    )

	def __str__(self):
 		return self.title


class Bookissue(models.Model):
	student= models.ForeignKey(Person, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete = models.CASCADE)
	given_date =models.DateTimeField(auto_now_add = True, auto_now= False)
	due_date = models.DateField()

class RequestBook(models.Model):
	yourname =models.ForeignKey(Person, on_delete=models.CASCADE)
	title = models.ForeignKey(Book, on_delete=models.CASCADE)
	catergory = models.ForeignKey(BookCatergory, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.yourname)

