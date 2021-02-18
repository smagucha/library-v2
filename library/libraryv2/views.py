from django.shortcuts import render, redirect
from .models import Book, BookCatergory, BookFormat, Person, Bookissue, Librarian
from .forms import BookForm, BookCatergoryForm, StudentForm,Issueform, Librarianform,requestbookform
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.db.models import Count
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def bookform(request):
  if request.user.is_authenticated:
  	form = BookForm(request.POST)
  	if request.method == 'POST':
  		form = BookForm(request.POST)
  		if form.is_valid():
  			form.save()
  			print(form)
  			form = BookForm()
  			return render(request, 'libraryv2/book_form.html')
  	else:
  		form = BookForm()
  	return render(request, 'libraryv2/book_form.html', {'form': form})
  else:
    return HttpResponseRedirect('login')

@login_required(login_url='/accounts/login/')
def allbook(request):
  if request.user.is_authenticated:
    if 'q' in request.GET:
          q=request.GET['q']
          lookup=(Q(title__icontains=q)|Q(subject__icontains=q)|Q(publisher__icontains=q)
            |Q(authors__icontains=q)|Q(nobooks__icontains=q))
          query =Book.objects.filter(lookup)
    else:
        query= Book.objects.all()
    return render(request, 'libraryv2/list_books.html', {'query': query})
  else:
    return HttpResponseRedirect('login')

@login_required(login_url='/accounts/login/')
def DeleteBook(request, id):
  if request.user.is_authenticated:
    delobj =Book.objects.get(id=id)
    if request.method == 'POST':
        delobj.delete()
        return redirect('allbooks')
    context = {
        'delobj': delobj
    }
    return render(request, 'libraryv2/deletebook.html', context)
  else:
    return HttpResponseRedirect('login')

@login_required(login_url='/accounts/login/')
def Updatebook(request, id):
  if request.user.is_authenticated:
  	obj = Book.objects.get(id=id)
  	form = BookForm(request.POST or None, instance= obj)
  	if form.is_valid():
  		form.save()
  		form= BookForm()
  		return redirect('allbooks')
  	return render(request, 'libraryv2/updatebook.html', {'obj':obj,'form': form})
  else:
    return HttpResponseRedirect('login')

@login_required(login_url='/accounts/login/')
def home(request):
  if request.user.is_authenticated:
    return render(request, 'libraryv2/home.html')
  else:
    return HttpResponseRedirect('login')

@login_required(login_url='/accounts/login/')
def Addbookcatergory(request):
  if request.user.is_authenticated:
    form = BookCatergoryForm(request.POST)
    if request.method == 'POST':
      form = BookCatergoryForm(request.POST)
      if form.is_valid():
        form.save()
        form = BookCatergoryForm()
        return render(request, 'libraryv2/Addbookcatergory.html')
    else:
      form = BookCatergoryForm()
    return render(request, 'libraryv2/Addbookcatergory.html', {'form': form})
  else:
    return HttpResponseRedirect('login')

@login_required(login_url='/accounts/login/')
def addstudent(request):
  if request.user.is_authenticated:
    form = StudentForm(request.POST)
    if request.method == 'POST':
      form = StudentForm(request.POST)
      if form.is_valid():
        form.save()
        form = StudentForm()
        return render(request,'libraryv2/addstudent.html',{'form': form})
    else:
      form = StudentForm()
      return render(request,'libraryv2/addstudent.html',{'form': form})
  else:
    return HttpResponseRedirect('login')

@login_required(login_url='/accounts/login/')
def liststudent(request):
  if request.user.is_authenticated:
    if 'q' in request.GET:
          q=request.GET['q']
          lookup=(Q(name__icontains=q)|Q(email__icontains=q)|Q(phone__icontains=q)
            |Q(studentid__icontains=q))
          student =Person.objects.filter(lookup)
    else:
        student= Person.objects.all()
    return render(request, 'libraryv2/liststudent.html', {'student': student})
  else:
    return HttpResponseRedirect('login')
@login_required(login_url='/accounts/login/')
def updatestudent(request, id):
  if request.user.is_authenticated:
    student = Person.objects.get(id=id)
    form = StudentForm(request.POST or None, instance= student)
    if form.is_valid():
      form.save()
      form= StudentForm()
      return redirect('liststudent')
    return render(request, 'libraryv2/updatestudent.html', {'student':student,'form': form})
  else:
    return HttpResponseRedirect('login')

@login_required(login_url='/accounts/login/')
def deletestudent(request, id):
  if request.user.is_authenticated:
    delstudent= Person.objects.get(id =id)
    if request.method=='POST':
      delstudent.delete()
      return redirect('liststudent')
    context = {
      'delstudent': delstudent
    }
    return render(request, 'libraryv2/deletestudent.html', context)
  else:
    return HttpResponseRedirect('login')


@login_required(login_url='/accounts/login/')
def Issuebook(request):
  if request.user.is_authenticated:
    form= Issueform(request.POST)
    if request.method =='POST':
      form= Issueform(request.POST)
      if form.is_valid():
        form.save()
        form =Issueform()
        return render(request,'libraryv2/issuebook.html', {'form': form})
    else:
      form = Issueform()
    return render(request, 'libraryv2/issuebook.html',{'form': form})
  else:
    return HttpResponseRedirect('login')

@login_required(login_url='/accounts/login/')
def Issuebookdelete(request, id):
  if request.user.is_authenticated:
    delbookissue = Bookissue.objects.get(id = id)
    if request.method=='POST':
      delbookissue.delete()
      return redirect('Issuedbooks')
    context = {
      'delbookissue': delbookissue
    }
    return render(request, 'libraryv2/deletebookissued.html', context)
  else:
    return HttpResponseRedirect('login')
@login_required(login_url='/accounts/login/')
def Issuebookupdate(request, id):
  if request.user.is_authenticated:
    updatebookissue=Bookissue.objects.get(id=id)
    form = Issueform(request.POST or None, instance= updatebookissue)
    if form.is_valid():
      form.save()
    return render(request,'libraryv2/Issuebookupdate.html',{'form':form})
  else:
    return HttpResponseRedirect('login')

@login_required(login_url='/accounts/login/')
def Issuedbooks(request):
  if request.user.is_authenticated:
    query =Bookissue.objects.all()
    return render(request, 'libraryv2/issuedbooks.html', {'query': query})
  else:
    return HttpResponseRedirect('login')

@login_required(login_url='/accounts/login/')
def studentdetail(request, id):
  if request.user.is_authenticated:
    student = Person.objects.filter(id = id) 
    x= Person.objects.get(id=id)
    y=x.bookissue_set.all()
    b =x.bookissue_set.count()
    print(y)
    context ={
      'student':student,
      'y':y,
      'b': b,
    }
    return render(request, 'libraryv2/studentdetail.html',context)
  else:
    return HttpResponseRedirect('login')


@login_required(login_url='/accounts/login/')
def Addlibrarian(request):
  if request.user.is_authenticated:
    form = Librarianform(request.POST)
    if request.method=='POST':
      form = Librarianform(request.POST)
      if form.is_valid():
        form.save()
        form=Librarianform()
        return render(request, 'libraryv2/addlibrarian.html', {'form': form})
    else:
      form = Librarianform()
      return render(request, 'libraryv2/addlibrarian.html', {'form': form})
  else:
    return HttpResponseRedirect('login')
@login_required(login_url='/accounts/login/')
def  librarianlist(request):
  if request.user.is_authenticated:
    liblist=Librarian.objects.all()
    return render(request, 'libraryv2/listlibrarian.html', {'liblist':liblist})
  else:
    return HttpResponseRedirect('login')

@login_required(login_url='/accounts/login/')
def updatelibrarian(request, id):
  if request.user.is_authenticated:
    liblistid = Librarian.objects.get(id = id)
    form = Librarianform(request.POST or None, instance=liblistid)
    if form.is_valid():
      form.save()
      form = Librarianform()
      return redirect('librarianlist')
    context={'liblistid':liblistid,'form':form , }
    return render(request, 'libraryv2/updatelibrarian.html', context)
  else:
    return HttpResponseRedirect('login') 
 
@login_required(login_url='/accounts/login/') 
def deletelibrarian(request, id):
  if request.user.is_authenticated:
    liblistid = Librarian.objects.get(id = id)
    if request.method=='POST':
      liblistid.delete()
      return redirect('listlibrarian')
    context = {
      'liblistid': liblistid
    }
    return render(request, 'libraryv2/deletelibrarian.html', context)
  else:
    return HttpResponseRedirect('login')
@login_required(login_url='/accounts/login/')
def requestbook(request, id):
  if request.user.is_authenticated:
    x= Person.objects.get(id=id)
    b =x.bookissue_set.count()
    if b >= 3:
      return render(request, 'libraryv2/norequestbook.html')
    else:
      form = requestbookform(request.POST)
      if request.method =='POST':
        form = requestbookform(request.POST)
        if form.is_valid():
          form.save()
          form = requestbookform()
          return render(request, 'libraryv2/requestbook.html', {'form':form})
      else:
        form = requestbookform()
        return render(request, 'libraryv2/requestbook.html',{'form':form})
  else:
    return HttpResponseRedirect('login')


  











































































































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




