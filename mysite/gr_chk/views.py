from django.shortcuts import render, get_object_or_404, redirect
from .models import Contract, Route
from .forms import ContractAddForm

# Create your views here.
def contract_list(request):
    contracts = Contract.objects.all().order_by('po')
    return render(request, 'gr_chk/contract_list.html', {'contracts':contracts})

def contract_detail(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    routes = Route.objects.filter(contract=pk)
    return render(request, 'gr_chk/contract_detail.html', {'contract': contract, 'routes':routes})

def contract_add(request):
    if request.method == "POST":
        form = ContractAddForm(request.POST)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.save()
            return redirect('contract_detail', pk=contract.pk)
    else:
        form = ContractAddForm()
    return render(request, 'gr_chk/contract_edit.html', {'form': form, 'title': 'เพิ่มข้อมูลสัญญา'})

def contract_edit(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == "POST":
        form = ContractAddForm(request.POST, instance=contract)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.save()
            return redirect('contract_detail', pk=contract.pk)
    else:
        form = ContractAddForm(instance=contract)
    return render(request, 'gr_chk/contract_edit.html', {'form': form, 'title': 'แก้ไขสัญญา'})
