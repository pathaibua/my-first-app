from django.db import models

# Create your models here.

class Contract(models.Model):
    contract_name = models.CharField(max_length=50)
    po = models.CharField(max_length=10)

    def __str__(self):
        return self.contract_name

class Route(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)

    def number():
        no = Route.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    route_order = models.IntegerField(default=number)
    plan_id = models.CharField(max_length=12)
    route_name = models.CharField(max_length=100)
    route_level = models.CharField(max_length=1)
    def __str__(self):
        return self.route_name

class boq(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    temp_pk = models.CharField(max_length=100)
    path = models.CharField(max_length=50)
    parent = models.CharField(max_length=50)
    item_name = models.CharField(max_length=200)
    unit_name = models.CharField(max_length=10, null=True)
    price_a = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    price_b = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    price_c = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    con_val = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.path
