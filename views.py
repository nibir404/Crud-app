from django.shortcuts import render, redirect

# Create your views here.
from .models import Insert


def index(request):
     data = Insert.objects.all()

     return render(request, 'index.html', {'data': data})


def create(request):
     print(request.POST)
     name = request.GET['name']
     f_name = request.GET['f_name']
     m_name = request.GET['m_name']
     age = request.GET['age']

     nibir = Insert(name=name, f_name=f_name, m_name=m_name, age=age)
     nibir.save()
     return redirect('/')


def delete(request, id):
     data = Insert.objects.get(pk=id)
     data.delete()
     return redirect('/')