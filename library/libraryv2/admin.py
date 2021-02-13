from django.contrib import admin

from .models import (
 	Book,BookFormat, Librarian,Person,BookCatergory,Bookissue
 	)
admin.site.register(BookFormat)
admin.site.register(Book)
admin.site.register(Librarian)
#admin.site.register(Person)
admin.site.register(BookCatergory)
admin.site.register(Bookissue)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email', 'phone',]
    list_display = ['name', 'email', 'phone',]

    #list_filter = []
