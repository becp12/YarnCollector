from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Yarn, Fibre
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
  id_list = yarn.fibre.all().values_list('id')
  fibre_yarn_doesnt_have = Fibre.objects.exclude(id__in=id_list)
  quantity_form = QuantityForm()
  return render(
    request,
    'yarns/detail.html',
    { 'yarn': yarn,
    'quantity_form': quantity_form,
    'fibre': fibre_yarn_doesnt_have})

class YarnCreate(CreateView):
  model = Yarn
  fields = ['brand', 'name', 'size', 'description', 'color']
  success_url = '/yarns/'

class YarnUpdate(UpdateView):
  model = Yarn
  fields = ['size', 'description', 'color']

class YarnDelete(DeleteView):
  model = Yarn
  success_url = '/yarns/'

def add_quantity(request, yarn_id):
  time = request.POST['time']
  mins = time[2:5]
  amPm = time[6:8]
  hrs = time[0:2]
  if amPm == 'PM':
    hrs = int(hrs) + 12
  time = f'{hrs}{mins}'
  post = request.POST.copy()
  post['time'] = time
  form = QuantityForm(post)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the yarn_id assigned
    new_quantity = form.save(commit=False)
    new_quantity.yarn_id = yarn_id
    new_quantity.save()
  return redirect('detail', yarn_id=yarn_id)

def assoc_fibre(request, yarn_id, fibre_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Yarn.objects.get(id=yarn_id).fibre.add(fibre_id)
  return redirect('detail', yarn_id=yarn_id)

def unassoc_fibre(request, yarn_id, fibre_id):
  Yarn.objects.get(id=yarn_id).fibre.remove(fibre_id)
  return redirect('detail', yarn_id=yarn_id)