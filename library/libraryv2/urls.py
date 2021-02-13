from django.urls import path
from . import views
urlpatterns=[
	path('', views.home),
	path('bookform', views.bookform),
	path('allbooks', views.allbook, name='allbooks'),
	path('deletebook/<int:id>/delete', views.DeleteBook),
	path('updatebook/<int:id>/update', views.Updatebook),
	path('bookcatergory', views.Addbookcatergory),
	path('addstudent', views.addstudent),
	path('liststudent', views.liststudent, name='liststudent'),
	path('updatestudent/<int:id>/update', views.updatestudent, ),
	path('deletestudent/<int:id>/delete', views.deletestudent),
	path('Issuebook', views.Issuebook),
	path('Issuedbooks', views.Issuedbooks),
	path('studentdetail/<int:id>/', views.studentdetail),
	path('returnbook', views.returnbook)
]

