from django.shortcuts import render

# Create your views here.
def contract_list(request):
    return render(request, 'gr_chk/contract_list.html', {})
