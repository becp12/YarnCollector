from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('yarns/', views.yarns_index, name='index'),
    path('yarns/<int:yarn_id>/', views.yarn_detail, name='detail'),
    path('yarns/create/', views.YarnCreate.as_view(), name='yarn_create'),
    path('yarns/<int:pk>/update/', views.YarnUpdate.as_view(), name='yarn_update'),
    path('yarns/<int:pk>/delete/', views.YarnDelete.as_view(), name='yarn_delete'),
    path('yarns/<int:yarn_id>/add_quantity/', views.add_quantity, name='add_quantity'),
    path('yarns/<int:yarn_id>/assoc_fibre/<int:fibre_id>/', views.assoc_fibre, name='assoc_fibre'),
    path('yarns/<int:yarn_id>/unassoc_fibre/<int:fibre_id>/', views.unassoc_fibre, name='unassoc_fibre'),
    path('fibres/', views.FibreList.as_view(), name='fibre_index'),
    path('fibres/<int:pk>/', views.FibreDetail.as_view(), name='fibre_detail'),
    path('fibres/create/', views.FibreCreate.as_view(), name='fibre_create'),
    path('fibres/<int:pk>/update/', views.FibreUpdate.as_view(), name='fibre_update'),
    path('fibres/<int:pk>/delete/', views.FibreDelete.as_view(), name='fibre_delete'),   
]