from django.urls import path
from . import views

urlpatterns = [
    path('', views.contract_list, name='contract_list'),
    path('<int:pk>/', views.contract_detail, name='contract_detail'),
    path('new/', views.contract_add, name='contract_add'),
    path('<int:pk>/edit/', views.contract_edit, name='contract_edit'),
]
