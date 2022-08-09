from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('yarns/', views.yarns_index, name='index'),
    path('yarns/<int:yarn_id>/', views.yarn_detail, name='detail'),
]