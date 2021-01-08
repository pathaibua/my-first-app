from django.contrib import admin
from .models import Contract, Route

class RouteInline(admin.TabularInline):
    model = Route
    extra = 3

class ContractAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['contract_name']}),
        (None,               {'fields': ['address']}),
        (None,               {'fields': ['po']}),
        (None,               {'fields': ['pr']}),
        (None,               {'fields': ['add_date']}),
        (None,               {'fields': ['status_name']}),
        #('Date information', {'fields': ['address']}),
    ]
    inlines = [RouteInline]
    list_display = ('contract_name', 'address', 'current_status')
    #list_filter = ['pub_date']
    #search_fields = ['question_text']


admin.site.register(Contract, ContractAdmin)
admin.site.register(Route)
