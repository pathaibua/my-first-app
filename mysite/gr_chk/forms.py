from django import forms

from .models import Contract

class ContractAddForm(forms.ModelForm):

    class Meta:
        model = Contract
        fields = ('contract_name', 'po',)
