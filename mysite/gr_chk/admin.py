from django.contrib import admin
from .models import Contract, Route, boq

# Register your models here.

class BoqInline(admin.TabularInline):
    model = boq
    extra = 1

class RouteInline(admin.TabularInline):
    model = Route
    extra = 1

class ContractAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['contract_name']}),
        (None,               {'fields': ['po']}),
        #(None,               {'fields': ['po']}),
        #(None,               {'fields': ['pr']}),
        #(None,               {'fields': ['add_date']}),
        #(None,               {'fields': ['status_name']}),
        #('Date information', {'fields': ['address']}),
    ]
    inlines = [RouteInline, BoqInline]
    list_display = ('contract_name', 'po')
    #list_filter = ['pub_date']
    search_fields = ['contract_name', 'po']

admin.site.register(Contract, ContractAdmin)
admin.site.register(Route)
