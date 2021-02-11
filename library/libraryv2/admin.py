from django.contrib import admin

from .models import (
 	Book,BookFormat, AccountStatus,
 	Librarian,Person, Rack, BookItem,BookCatergory
 	)
admin.site.register(BookFormat)
admin.site.register(Book)
admin.site.register(AccountStatus)
admin.site.register(Librarian)
admin.site.register(Person)
admin.site.register(BookItem)
admin.site.register(Rack)
admin.site.register(BookCatergory)

