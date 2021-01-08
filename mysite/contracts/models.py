import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Vendor(models.Model):
    vendor_id = models.CharField(primary_key=True, max_length = 10, unique = True)
    vendor_name = models.CharField('ชื่อผู้รับจ้าง', max_length = 50, unique = True)

    def __str__(self):
        return self.vendor_name

class Contract(models.Model):
    contract_name = models.CharField('ชื่อสัญญา', max_length = 50, unique = True)
    address = models.CharField('สถานที่', max_length = 200, default = '')
    pr = models.CharField(max_length = 10, blank = True)
    po = models.CharField(max_length = 10, blank = True)
    add_date = models.DateTimeField('date added')
    po_date = models.DateTimeField('PO date', blank = True)
    start_date = models.DateTimeField('PO start date', blank = True)
    end_date = models.DateTimeField('PO end date', blank = True)
    vendor = models.ForeignKey(Vendor, on_delete = models.CASCADE)

    STATUS_NAME = (
        ('0', 'เบิกจ้าง'),
        ('1', 'จัดทำ TOR/ราคากลาง'),
        ('2', 'รองบประมาณ'),
        ('3', 'ประกวดราคา'),
        ('4', 'อื่นๆ'),
    )

    status_name = models.CharField(max_length = 2, choices = STATUS_NAME, default = '0')

    def __str__(self):
        return self.contract_name

    def current_status(self):
        #return self.status_name
        return self.get_status_name_display()

    current_status.short_description = 'สถานะ'

class Route(models.Model):
    contract = models.ForeignKey(Contract, on_delete = models.CASCADE)
    route_no = models.CharField(max_length = 12, unique = True)
    route_name = models.CharField(max_length = 200)
    Route_Level = models.TextChoices('route_level','A B C')
    route_level = models.CharField(blank=True, choices=Route_Level.choices, max_length=1)
    price_E = models.DecimalField(max_digits = 19, decimal_places = 4, blank = True)
    price_W = models.DecimalField(max_digits = 19, decimal_places = 4, blank = True)
    route_dma = models.CharField(max_length = 6, blank = True)

    def __str__(self):
        return self.route_name

class Wbs(models.Model):
    wbs = models.CharField(max_length = 12, unique = True)
    con_type = models.ForeignKey(Contract, on_delete = models.CASCADE)
    amt = models.DecimalField(max_digits = 19, decimal_places = 4, blank = True)

    WBS_TYPE = (
        ('0', 'ไม่ระบุ'),
        ('1', 'ค่าแรง'),
        ('2', 'ค่าท่อ'),
    )

    wbs_type = models.CharField(max_length = 2, choices = WBS_TYPE, default = '0')

    def __str__(self):
        return self.wbs

    def type(self):
        return self.get_wbs_type_display()
