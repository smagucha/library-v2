from django.shortcuts import render
from .models import Book
from .forms import BookForm

def Book(request):
	form = BookForm(request.POST)
	if request.method == 'POST':
		orm = BookForm(request.POST)
		if form.is_valid():
			form.save()
			print(form)
			form = BookForm()
			return render(request, 'libraryv2/book_form.html')
	else:
		form = BookForm()
	return render(request, 'libraryv2/book_form.html', {'form': form})









































































































"""
class BookFormat(Enum):
  HARDCOVER, PAPERBACK, AUDIO_BOOK, EBOOK, NEWSPAPER, MAGAZINE, JOURNAL = 1, 2, 3, 4, 5, 6, 7


class BookStatus(Enum):
  AVAILABLE, RESERVED, LOANED, LOST = 1, 2, 3, 4


class ReservationStatus(Enum):
  WAITING, PENDING, CANCELED, NONE = 1, 2, 3, 4


class AccountStatus(Enum):
  ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE = 1, 2, 3, 4, 5



from abc import ABC, abstractmethod

class Search(ABC):
  def search_by_title(self, title):
    None

  def search_by_author(self, author):
    None

  def search_by_subject(self, subject):
    None

  def search_by_pub_date(self, publish_date):
    None


class Catalog(Search):
  def __init__(self):
    self.__book_titles = {}
    self.__book_authors = {}
    self.__book_subjects = {}
    self.__book_publication_dates = {}

  def search_by_title(self, query):
    # return all books containing the string query in their title.
    return self.__book_titles.get(query)

  def search_by_author(self, query):
    # return all books containing the string query in their author's name.
    return self.__book_authors.get(query)

from abc import ABC, abstractmethod

class Book(ABC):
  def __init__(self, ISBN, title, subject, publisher, language, number_of_pages):
    self.__ISBN = ISBN
    self.__title = title
    self.__subject = subject
    self.__publisher = publisher
    self.__language = language
    self.__number_of_pages = number_of_pages
    self.__authors = []


class BookItem(Book):
  def __init__(self, barcode, is_reference_only, borrowed, due_date, price, book_format, status, date_of_purchase, publication_date, placed_at):
    self.__barcode = barcode
    self.__is_reference_only = is_reference_only
    self.__borrowed = borrowed
    self.__due_date = due_date
    self.__price = price
    self.__format = book_format
    self.__status = status
    self.__date_of_purchase = date_of_purchase
    self.__publication_date = publication_date
    self.__placed_at = placed_at

  def checkout(self, member_id):
    if self.get_is_reference_only():
      print("self book is Reference only and can't be issued")
      return False
    if not BookLending.lend_book(self.get_bar_code(), member_id):
      return False
    self.update_book_item_status(BookStatus.LOANED)
    return True


class Rack:
  def __init__(self, number, location_identifier):
    self.__number = number
    self.__location_identifier = location_identifier


 class BookReservation:
  def __init__(self, creation_date, status, book_item_barcode, member_id):
    self.__creation_date = creation_date
    self.__status = status
    self.__book_item_barcode = book_item_barcode
    self.__member_id = member_id

  def fetch_reservation_details(self, barcode):
    None


class BookLending:
  def __init__(self, creation_date, due_date, book_item_barcode, member_id):
    self.__creation_date = creation_date
    self.__due_date = due_date
    self.__return_date = None
    self.__book_item_barcode = book_item_barcode
    self.__member_id = member_id

  def lend_book(self, barcode, member_id):
    None

  def fetch_lending_details(self, barcode):
    None


class Fine:
  def __init__(self, creation_date, book_item_barcode, member_id):
    self.__creation_date = creation_date
    self.__book_item_barcode = book_item_barcode
    self.__member_id = member_id

  def collect_fine(self, member_id, days):
    None


"""




