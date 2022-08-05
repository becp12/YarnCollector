from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Yarn:  # Note that parens are optional if not inheriting from another class
  def __init__(self, brand, name, size, description, color):
    self.brand = brand
    self.name = name
    self.size = size
    self.description = description
    self.color = color

yarns = [
  Yarn('Lion Brand', '24/7 Cotton', '4/Medium/Worsted', 'A soft cotton, great for clothing', 'Sky'),
  Yarn('Bernat', 'Blanket', '6/Super Bulky', 'Great yarn for making thick & warm blankets', 'Crimson'),
  Yarn('Big Twist', 'Value', '4/Medium/Worsted', 'Great value yarn, useful for a variety of projects', 'Varsity Yellow')
]
# Create your views here.
# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Yarn Lovers!</h1>')

def about(request):
    return render(request, 'about.html')

def yarns_index(request):
    return render(request, 'yarns/index.html', { 'yarns': yarns })