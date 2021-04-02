from django import forms
from django.forms import ModelForm
from .models import Book, BookCatergory,Person, Bookissue, Librarian ,RequestBook

class BookForm(ModelForm):
	class Meta:
		model = Book
		exclude = ['givenout']
	


class BookCatergoryForm(ModelForm):
	class Meta:
		model= BookCatergory
		fields = '__all__'

class StudentForm(ModelForm):
	class Meta:
		model = Person
		fields = ('user','phone','studentid')
		# widgets={
		# 	'user':forms.TextInput(attrs={'class':'form-group','placeholder':'user','id':'user', 'disable':True}), 
		# 	'phone': forms.TextInput(attrs={'class':'form-group'}),
		# 	'studentid': forms.TextInput(attrs={'class':'form-group'}),
		# }
		#forms.TextField(widget=widgets.Select)

class Issueform(ModelForm):
	class Meta:
		model = Bookissue
		fields ='__all__'

class Librarianform(ModelForm):
	class Meta:
		model = Librarian
		fields ='__all__'

class requestbookform(forms.ModelForm):
	class Meta:
		model = RequestBook
		fields =('yourname','title','catergory')

		


