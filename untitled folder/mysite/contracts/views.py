
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Contract




class IndexView(generic.ListView):
    template_name = 'contracts/index.html'
    context_object_name = 'Test_Con'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Contract.objects
