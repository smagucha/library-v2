from django.contrib import admin

from .models import (
	Book,ReservationStatus,BookStatus,BookFormat, AccountStatus,
	Librarian,Person, Rack, BookItem
	)

admin.site.register(BookFormat)
admin.site.register(Book)
admin.site.register(ReservationStatus)
admin.site.register(BookStatus)
admin.site.register(AccountStatus)
admin.site.register(Librarian)
admin.site.register(Person)
admin.site.register(BookItem)
admin.site.register(Rack)
