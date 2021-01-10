from django.urls import path
from . import views

urlpatterns = [
    path('', views.contract_list, name='contract_list'),
    path('contract/<int:pk>/', views.contract_detail, name='contract_detail'),
    path('newcontract/', views.contract_add, name='contract_add'),
    path('contract/<int:pk>/edit/', views.contract_edit, name='contract_edit'),
    path('contract/<int:pk>/newroute/', views.route_add, name='route_add'),
    path('route/<int:pk>/edit/', views.route_edit, name='route_edit'),
]
