from django import forms

from .models import Contract, Route

class ContractAddForm(forms.ModelForm):

    class Meta:
        model = Contract
        fields = ('contract_name', 'po',)

class RouteAddForm(forms.ModelForm):

    class Meta:
        model = Route
        fields = ('plan_id', 'route_name', 'route_level')
