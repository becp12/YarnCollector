from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Yarn
from .forms import QuantityForm
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
  quantity_form = QuantityForm()
  return render(
    request,
    'yarns/detail.html',
    { 'yarn': yarn, 'quantity_form': quantity_form })

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

def add_quantity(request, yarn_id):
  form = QuantityForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_quantity = form.save(commit=False)
    new_quantity.yarn_id = yarn_id
    new_quantity.save()
  return redirect('detail', yarn_id=yarn_id)