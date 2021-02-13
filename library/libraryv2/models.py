from django.db import models

class Person(models.Model):
	name = models.CharField(max_length= 200)
	email = models.EmailField()
	phone =models.PositiveIntegerField()
	studentid = models.CharField(max_length= 200)

class Librarian(models.Model):
	name = models.CharField(max_length= 200)
	email = models.EmailField()
	phone =models.PositiveIntegerField()
	librarianid = models.CharField(max_length= 200)


class AccountStatus(models.Model):
	Active= 'Active'
	Closed= 'closed'
	Canceled= 'Canceled'
	Blacklisted='Blacklisted'
	Nill = 'Nill'
	Account = (
        (Active, 'Active'),
    	(Closed, 'closed'),
    	(Canceled, 'Canceled'),
    	(Blacklisted, 'Blacklisted'),
    	(Nill , 'Nill'),
    )
	statusaccount = models.CharField(
        max_length=11,
        choices=Account,
        default=Nill,
    )
	"""
	def is_status(self):
		return self.Account in {
       	self.AccountStatus.Active,
        self.AccountStatus.Closed,
        self.AccountStatus.Canceled,
        self.AccountStatus.Blacklisted,
        self.AccountStatus.Nill,
        }
    """
 

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
	 
class Rack(models.Model):
	location_identifier = models.CharField(max_length= 300)

class BookItem(models.Model):
 	book = models.ForeignKey(Book, on_delete= models.CASCADE)
 	borrowed = models.BooleanField(default=False)
 	due_date = models.DateField()
 	price = models.PositiveIntegerField()
 	rack =models.ForeignKey(Rack, on_delete= models.CASCADE)


 	
  	
 
