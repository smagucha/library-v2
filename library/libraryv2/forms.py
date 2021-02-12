from django.forms import ModelForm
from .models import Book, BookCatergory,Person

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