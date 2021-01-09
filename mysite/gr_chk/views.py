from django.shortcuts import render
from .models import Contract

# Create your views here.
def contract_list(request):
    contracts = Contract.objects.all().order_by('po')
    return render(request, 'gr_chk/contract_list.html', {'contracts':contracts})
