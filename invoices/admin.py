from django.contrib import admin

from invoices.models import Invoice, Item, ItemPackaging, OrderItem, Year

admin.site.register(Invoice)
admin.site.register(Item)
admin.site.register(ItemPackaging)
admin.site.register(OrderItem)
admin.site.register(Year)
