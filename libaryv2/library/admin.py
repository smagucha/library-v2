from django.contrib import admin
from .models import Student, Registerbook, Librarian, Publisher, Author

#admin.site.register(Student)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields=['name','admin_no',]
    list_display=['name', 'admin_no', 'course', 'faculty',]
    list_filter=['name','admin_no']
admin.site.register(Registerbook)
admin.site.register(Librarian)
admin.site.register(Author)
admin.site.register(Publisher)
