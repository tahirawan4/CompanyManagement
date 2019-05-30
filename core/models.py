from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Supplier(BaseModel):
    name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField()
    phone = PhoneNumberField(blank=True, default=None, null=True)

    def __str__(self):
        return self.name


class Buyer(BaseModel):
    name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField()
    phone = PhoneNumberField(blank=True, default=None, null=True)

    def __str__(self):
        return self.name


class Truck(BaseModel):
    plat_number = models.CharField(max_length=100)
    license = models.CharField(max_length=200, null=True, blank=True)

    def __str(self):
        return self.plat_number


class TruckDriver(BaseModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phone = PhoneNumberField(blank=True, default=None, null=True)
    trucks = models.ManyToManyField(Truck, null=True, blank=True)

    def __str__(self):
        return self.first_name
