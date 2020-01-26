from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.db.models import Q
from library import models
from library.models import Student, Registerbook, Librarian, Author, Publisher
from .forms import MyForm, registerstudent
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


# from django.urls import reverse_lazy
class home(LoginRequiredMixin, View):
    template_name = 'library/home.html'

    def get(self, request):
        return render(request, self.template_name)


class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')


class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)


class MyFormView(LoginRequiredMixin, View):
    login_url = '/login/'
    form_class = MyForm
    # initial = {'key': 'value'}
    template_name = 'library/form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')
        return render(request, self.template_name, {'form': form})


class studentregister(LoginRequiredMixin, View):
    login_url = '/login/'
    form = registerstudent
    template_name = 'library/registerstudent.html'

    def get(self, request, *args, **kwargs):
        form = self.form()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            form = registerstudent()
            return HttpResponseRedirect('success')
        else:
            form = registerstudent()
        return render(request, {'form': form}, self.template_name)


class success(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'library/success.html')


class studentMixin:
    login_url = '/login/'
    model = Student
    fields = '__all__'
    success_url = "liststudent"


class liststudent(LoginRequiredMixin, studentMixin, ListView):
    success_url = "liststudent"


class createstudent(LoginRequiredMixin, studentMixin, CreateView):
    pass


class updatestudent(LoginRequiredMixin, studentMixin, UpdateView):
    pass


class deletestudent(LoginRequiredMixin, studentMixin, DeleteView):
    pass


"""   


class liststudent(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Student


class createstudent(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Student
    fields = '__all__'
    success_url = "liststudent"


class updatestudent(LoginRequiredMixin, UpdateView):
    model = Student
    fields = '__all__'
    

class deletestudent(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Student
    success_url = 'liststudent'

"""


class bookMixin:
    login_url = '/login/'
    model = Registerbook
    fields = '__all__'
    success_url = 'success'


class createbook(LoginRequiredMixin, bookMixin, CreateView):
    pass


class updatebook(LoginRequiredMixin, bookMixin, UpdateView):
    pass


class listbook(LoginRequiredMixin, bookMixin, ListView):
    pass


class deletebook(LoginRequiredMixin, bookMixin, DeleteView):
    pass


""" 
class createbook(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Registerbook
    fields = '__all__'
    success_url = 'success'


class updatebook(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Registerbook
    fields = '__all__'


class listbook(LoginRequiredMixin, ListView):
    model = Registerbook


class deletebook(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Registerbook
    success_url = 'listbook'
"""


class librarianMixin:
    login_url = '/login/'
    model = Librarian
    fields = '__all__'
    success_url = 'listlibrarian'


class createlibrarian(LoginRequiredMixin, librarianMixin, CreateView):
    pass


class listlibrarian(LoginRequiredMixin, librarianMixin, ListView):
    pass


class deletelibrarian(LoginRequiredMixin, librarianMixin, DeleteView):
    pass


class updatelibrarian(LoginRequiredMixin, librarianMixin, UpdateView):
    pass


"""
class createlibrarian(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Librarian
    fields = '__all__'
    success_url = 'listlibrarian'


class listlibrarian(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Librarian



class deletelibrarian(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Librarian
    success_url = 'listlibrarian'


class updatelibrarian(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Librarian
    fields = '__all__'
"""


class authorMixin:
    login_url = '/login/'
    model = Author
    fields = '__all__'
    success_url = 'success'


class createauthor(LoginRequiredMixin, authorMixin, CreateView):
    pass


class updateauthor(LoginRequiredMixin, authorMixin, UpdateView):
    pass


class listauthor(LoginRequiredMixin, authorMixin, ListView):
    pass


class deleteauthor(LoginRequiredMixin, authorMixin, DeleteView):
    pass


""" 
class createauthor(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Author
    fields = '__all__'
    success_url = 'success'


class updateauthor(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Author
    fields = '__all__'
    success_url = 'success'


class listauthor(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Author


class deleteauthor(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Author
    success_url = 'listauthor'

"""


class publiserMixin:
    model = models.Publisher
    fields = '__all__'
    login_url = '/login/'
    success_url = 'success'


class createpublisher(LoginRequiredMixin, publiserMixin, CreateView):
    pass


class updatepublisher(LoginRequiredMixin, publiserMixin, UpdateView):
    pass


class listpublisher(LoginRequiredMixin, publiserMixin, ListView):
    pass


class deletepublisher(LoginRequiredMixin, publiserMixin, DeleteView):
    pass


def searchbook(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
                Q(name__icontains=query) |
                Q(author__name__icontains=query) |
                Q(publisher__name__icontains=query)
        )
        results = Registerbook.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("library/searchbook.html", {"results": results, "query": query})


"""
class createpublisher(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Publisher
    fields ='__all__'
    success_url = 'success'


class updatepublisher(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    model= Publisher
    fields = '__all__'
    success_url = 'success'


class listpublisher(ListView):
    model = Publisher

class deletepublisher(DeleteView):
    model = Publisher
    success_url = 'listauthor'
"""



