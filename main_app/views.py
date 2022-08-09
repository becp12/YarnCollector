from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Yarn
# Add the following import
from django.http import HttpResponse

# Create your views here.
# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def yarns_index(request):
  yarns = Yarn.objects.all()
  return render(request, 'yarns/index.html', { 'yarns': yarns })

def yarn_detail(request, yarn_id):
  yarn = Yarn.objects.get(id=yarn_id)
  return render(request, 'yarns/detail.html', { 'yarn': yarn })

class YarnCreate(CreateView):
  model = Yarn
  fields = '__all__'
  success_url = '/yarns/'

class YarnUpdate(UpdateView):
  model = Yarn
  fields = ['size', 'description', 'color']

class YarnDelete(DeleteView):
  model = Yarn
  success_url = '/yarns/'