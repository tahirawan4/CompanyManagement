from django.db import models

from core.models import BaseModel, Supplier, Buyer, TruckDriver, Truck
from products.models import Item, ItemPackaging


class OrderItem(BaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    item_packaging = models.ForeignKey(ItemPackaging, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Invoice(BaseModel):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    order_items = models.ManyToManyField(OrderItem)
    truck_driver = models.ForeignKey(TruckDriver, on_delete=models.CASCADE)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    date_pick_up = models.DateField(null=True, blank=True)
    place_of_pickup = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)
