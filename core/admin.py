from django.contrib import admin

from core.models import Supplier, Buyer, Truck, TruckDriver

admin.site.register(Supplier)
admin.site.register(Buyer)
admin.site.register(Truck)
admin.site.register(TruckDriver)
