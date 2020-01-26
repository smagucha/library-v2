from django.urls import path
from . import  views
from .views import (
    MyView, GreetingView, MyFormView, studentregister, success, liststudent,
    createstudent, updatestudent, deletestudent, home, createbook, updatebook, listbook, deletebook, createlibrarian,
    listlibrarian, deletelibrarian, updatelibrarian, createauthor, updateauthor, listauthor, deleteauthor,
    createpublisher,
    updatepublisher, listpublisher, deletepublisher

)

urlpatterns = (
    path('', home.as_view()),
    path('about/', MyView.as_view()),
    path('greeting/', GreetingView.as_view(greeting="G'day")),
    path('myform', MyFormView.as_view()),
    path('studentregister', studentregister.as_view()),
    path('success', success.as_view()),
    path('liststudent', liststudent.as_view(), name='liststudent'),
    path('createstudent', createstudent.as_view()),
    path('updatestudent/<int:pk>/', updatestudent.as_view()),
    path('deletestudent/<int:pk>/', deletestudent.as_view()),
    path('createbook', createbook.as_view()),
    path('updatebook/<int:pk>', updatebook.as_view()),
    path('listbook', listbook.as_view()),
    path('deletebook/<int:pk>', deletebook.as_view()),
    path('createlibrarian', createlibrarian.as_view()),
    path('listlibrarian', listlibrarian.as_view()),
    path('deletelibrarian/<int:pk>',deletelibrarian.as_view()),
    path('updatelibrarian/<int:pk>', updatelibrarian.as_view()),
    path('createauthor', createauthor.as_view()),
    path('updateauthor/<int:pk>', updateauthor.as_view()),
    path('listauthor',listauthor.as_view()),
    path('deleteauthor/<int:pk>',deleteauthor.as_view()),
    path('createpublisher', createpublisher.as_view()),
    path('updatepublisher/<int:pk>', updatepublisher.as_view()),
    path('listpublisher',listpublisher.as_view()),
    path('deletepublisher/<int:pk>',deletepublisher.as_view()),
    path('searchbook',views.searchbook),

)
