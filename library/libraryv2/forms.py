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
		fields = '__all__'

	def clean_user(self):
		user = self.cleaned_data.get('user')
		for instance in Person.objects.all():
			if instance.user == user:
				raise forms.ValidationError('We have a student with the same details', user)
		return user

class Issueform(ModelForm):
	class Meta:
		model = Bookissue
		fields ='__all__'

class Librarianform(ModelForm):
	class Meta:
		model = Librarian
		fields ='__all__'

	def clean_user(self):
		user = self.cleaned_data.get('user')
		for instance in Librarian.objects.all():
			if instance.user == user:
				raise forms.ValidationError('We have a librarian with the same details', user)

class requestbookform(forms.ModelForm):
	class Meta:
		model = RequestBook
		fields ='__all__'

		
class BookIssueform(forms.ModelForm):
	class Meta:
		model= Bookissue
		fields ='__all__'

