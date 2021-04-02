from django.urls import path
from . import views
urlpatterns=[
	path('', views.home, name=''),
	path('bookform', views.bookform),
	path('allbooks', views.allbook, name='allbooks'),
	path('deletebook/<int:id>/delete', views.DeleteBook, name='deletebook'),
	path('updatebook/<int:id>/update', views.Updatebook, name='updatebook'),
	path('bookcatergory', views.Addbookcatergory , name= 'bookcatergory'),
	path('addstudent', views.addstudent, name='addstudent'),
	path('liststudent', views.liststudent, name='liststudent'),
	path('updatestudent/<int:id>/update', views.updatestudent, name='updatestudent' ),
	path('deletestudent/<int:id>/delete', views.deletestudent, name='deletestudent'),
	path('Issuebook/<int:id>', views.Issuebook, name= 'Issuebook'),
	path('Issuedbooks', views.Issuedbooks, name='Issuedbooks'),
	path('studentdetail/<int:id>/', views.studentdetail, name='studentdetail'),
	path('Addlibrarian', views.Addlibrarian, name='Addlibrarian'),
	path('librarianlist', views.librarianlist, name='librarianlist'),
	path('updatelibrarian/<int:id>/update', views.updatelibrarian, name='updatelibrarian' ),
	path('deletelibrarian/<int:id>/delete', views.deletelibrarian, name='deletelibrarian'),
	path('requestbook/<int:id>/', views.requestbook, name='requestbook'),
	path('deletebookissue/<int:id>/delete', views.Issuebookdelete, name='issuebookdelete'),
	path('Issuebookupdate/<int:id>/update', views.Issuebookupdate, name='issuebookupdate' ),
	path('requestedbooks', views.requestedbooks, name='requestedbooks'),
	path('Bookcatergory', views.Bookcatergory, name='Bookcatergory'),
	
	
	
]
