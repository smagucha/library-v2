from django.urls import path
from . import views
urlpatterns=[
	path('', views.home),
	path('bookform', views.bookform),
	path('allbooks', views.allbook, name='allbook'),
	path('deletebook/<int:id>/delete', views.DeleteBook),
	path('updatebook/<int:id>/update', views.Updatebook),
	path('bookcatergory', views.Addbookcatergory),

]

