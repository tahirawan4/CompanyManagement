from django.db import models

from core.models import BaseModel, Supplier, Buyer, TruckDriver, Truck
from products.models import Item, ItemPackaging
from phonenumber_field.modelfields import PhoneNumberField


class Company(BaseModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = PhoneNumberField()
    email = models.EmailField()
    PIB = models.CharField(max_length=9)
    MB = models.CharField(max_length=8)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Companies'
