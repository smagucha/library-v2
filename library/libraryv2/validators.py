from libaryv2.models import Book
from django.core.validators import RegexValidator


bookavail = Book.objects.get(id = 1)
print(bookavail)
