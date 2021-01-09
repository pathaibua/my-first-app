from django.shortcuts import render, get_object_or_404
from .models import Contract

# Create your views here.
def contract_list(request):
    contracts = Contract.objects.all().order_by('po')
    return render(request, 'gr_chk/contract_list.html', {'contracts':contracts})

def contract_detail(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    return render(request, 'gr_chk/contract_detail.html', {'contract': contract})
