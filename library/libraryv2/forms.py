from django.forms import ModelForm
from .models import Book, BookCatergory,Person, Bookissue, Librarian,RequestBook

class BookForm(ModelForm):
	class Meta:
		model = Book
		fields ='__all__'

class BookCatergoryForm(ModelForm):
	class Meta:
		model= BookCatergory
		fields = '__all__'

class StudentForm(ModelForm):
	class Meta:
		model = Person
		fields = '__all__'

class Issueform(ModelForm):
	class Meta:
		model = Bookissue
		fields ='__all__'

class Librarianform(ModelForm):
	class Meta:
		model = Librarian
		fields ='__all__'

class requestbookform(ModelForm):
	class Meta:
		model = RequestBook
		fields ='__all__'
