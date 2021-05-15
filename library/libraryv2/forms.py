from django import forms
from django.forms import ModelForm
from .models import Book, BookCatergory,Person, Bookissue, Librarian ,RequestBook
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

#User.objects.filter(groups__name='monkeys')
User = get_user_model()
class DateInput(forms.DateInput):
    input_type = 'date'

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
		usergroup = User.objects.filter(groups__name='studentgroup')
		user = self.cleaned_data.get('user')
		print(user)

		# if user not in usergroup:
		# 	raise forms.ValidationError('user is not a student')
		# else:
		for instance in Person.objects.all() :
			if instance.user == user:
				raise forms.ValidationError('We have a student with the same details')
				print(instance.user)
			else:
				return user
				print(instance.user)
		return user

		def clean_studentid(self):
			Studentid = self.cleaned_data.get('studentid')
			print(Studentid)
			for instance in Person.objects.all() :
				if instance.studentid == Studentid:
					raise forms.ValidationError('We have a student with the same ID')
					print(instance.studentid)
				else:
					return Studentid
					print(instance.studentid)
			return Studentid

		def clean_phone(self):
			Phone = self.cleaned_data.get('Phone')
			print(Phone)
			for instance in Person.objects.all() :
				if instance.phone == Phone:
					raise forms.ValidationError('We have a student with the same phone number')
					print(instance.phone)
				else:
					return Phone
					print(instance.user)
			return Phone


class Issueform(ModelForm):
	class Meta:
		model = Bookissue
		fields ='__all__'
		widgets = { 'due_date': DateInput() }

	



class Librarianform(ModelForm):
	class Meta:
		model = Librarian
		fields ='__all__'

	def clean_user(self):
		user = self.cleaned_data.get('user')
		for instance in Librarian.objects.all():
			if instance.user == user:
				raise forms.ValidationError('We have a librarian with the same details')
		return user

class requestbookform(forms.ModelForm):
	class Meta:
		model = RequestBook
		fields ='__all__'


