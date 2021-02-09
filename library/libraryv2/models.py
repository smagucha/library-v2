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
	"""
	def is_bookformatt(self):
		return self.year_in_school in {
		self.BookFormat.HARDCOVER,
        self.BookFormat.PAPERBACK,
        self.BookFormat.NEWSPAPER,
        self.BookFormat.MAGAZINE,
        self.BookFormat.JOURNAL,
       }
"""
class BookStatus(models.Model):
	AVAILABLE = 'AVAILABLE'
	RESERVED = 'RESERVED'
	LOANED ='LOANED'
	LOST ='LOST'

	status =(
		(AVAILABLE, 'AVAILABLE'),
  		(RESERVED, 'RESERVED'),
  		(LOANED,'LOANED'),
  		(LOST, 'LOST'),
	)
	bookstatus = models.CharField(
		max_length=9,
		choices=status,
		default=AVAILABLE,
    )
	"""
	def is_bookstatus(self):
		return self.year_in_school in {
		self.BookStatus.AVAILABLE,
        self.BookStatus.RESERVED,
        self.BookStatus.LOANED,
        self.BookStatus.LOST,
        }
    """
 
class ReservationStatus(models.Model):
	WAITING ='WAITING'
	CANCELED='CANCELED'
	NONE='NONE'
	status =(
		(WAITING, 'WAITING'),
  		(CANCELED,'CANCELED'),
  		(NONE, 'NONE'),
  		)
	resstatus = models.CharField(max_length=8, choices=status,default=NONE,)
	"""
	def is_resstatus(self):
		return self.status in {
       	self.ReservationStatus.WAITING,
        self.ReservationStatus.CANCELED,
        self.ReservationStatus.NONE,
       }
  		
	"""
class BookCatergory(models.Model):
	name= models.CharField(max_length= 200)

class Book(models.Model):
	title = models.CharField(max_length = 200)
	subject = models.CharField(max_length= 200)
	publisher = models.CharField(max_length= 200)
	authors = models.CharField(max_length= 200)
	nobooks = models.PositiveIntegerField()
	 
class Rack(models.Model):
	location_identifier = models.CharField(max_length= 300)

class BookItem(models.Model):
 	book = models.ForeignKey(Book, on_delete= models.CASCADE)
 	borrowed = models.BooleanField(default=False)
 	due_date = models.DateField()
 	price = models.PositiveIntegerField()
 	book_format = models.ForeignKey(BookStatus, on_delete=models.CASCADE)
 	rack =models.ForeignKey(Rack, on_delete= models.CASCADE)
  	
 
