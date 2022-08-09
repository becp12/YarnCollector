from django.shortcuts import render
from .models import Yarn
# Add the following import
from django.http import HttpResponse

# Create your views here.
# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Yarn Lovers!</h1>')

def about(request):
    return render(request, 'about.html')

def yarns_index(request):
  yarns = Yarn.objects.all()
  return render(request, 'yarns/index.html', { 'yarns': yarns })

def yarn_detail(request, yarn_id):
  yarn = Yarn.objects.get(id=yarn_id)
  return render(request, 'yarns/detail.html', { 'yarn': yarn })