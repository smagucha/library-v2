from django.forms import ModelForm
from .models import Book, BookCatergory

class BookForm(ModelForm):
	class Meta:
		model = Book
		fields ='__all__'

class BookCatergoryForm(ModelForm):
	class Meta:
		model= BookCatergory
		fields = '__all__'