from django.shortcuts import render
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def finchs_index(request):
    finchs = Finch.objects.all()
    return render(request, 'finchs/index.html', { 'finchs': finchs})

def finchs_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finchs/detail.html', { 'finch': finch})

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'height', 'vertical']

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'height', 'vertical']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finchs/'
