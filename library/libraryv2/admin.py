from django.contrib import admin

from .models import (
 	Book,BookFormat, Librarian,Person,BookCatergory,Bookissue
 	)
# admin.site.register(BookFormat)
# admin.site.register(Book)
# admin.site.register(Librarian)
# #admin.site.register(Person)
# admin.site.register(BookCatergory)
# admin.site.register(Bookissue)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email', 'phone',]
    list_display = ['name', 'email', 'phone',]
    #list_filter = []

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'subject', 'publisher','authors',]
    list_display = ['title', 'subject', 'publisher','authors']
    #list_filter = []

@admin.register(Bookissue)
class BookissueAdmin(admin.ModelAdmin):
    search_fields = ['student', 'book', 'given_date','due_date',]
    list_display = ['student', 'book', 'given_date','due_date',]
    #list_filter = []


   