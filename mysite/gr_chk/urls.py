from django.urls import path
from . import views

urlpatterns = [
    path('', views.contract_list, name='contract_list'),
    path('gr_chk/<int:pk>/', views.contract_detail, name='contract_detail'),
]
