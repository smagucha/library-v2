from django.contrib import admin

from .models import (
 	Book, Librarian,Person,BookCatergory,Bookissue, RequestBook
 	)

# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     search_fields = ['name', 'email', 'phone',]
#     list_display = ['name', 'email', 'phone',]
#     #list_filter = []
admin.site.register(Person)
admin.site.register(RequestBook)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'subject', 'publisher','authors',]
    list_display = ['title', 'subject', 'publisher','authors','availablebook','givenout']
    #list_filter = []

@admin.register(Bookissue)
class BookissueAdmin(admin.ModelAdmin):
    search_fields = ['student', 'book', 'given_date','due_date',]
    list_display = ['student', 'book', 'given_date','due_date',]
    #list_filter = []


admin.site.register(Librarian)
# @admin.register(Librarian)
# class LibrarianAdmin(admin.ModelAdmin):
#     search_fields = ['name', 'email', 'phone','librarianid',]
#     list_display = ['name', 'email', 'phone','librarianid',]
    #list_filter = []

@admin.register(BookCatergory)
class BookCatergoryAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
    list_display = ['name', ]


   
