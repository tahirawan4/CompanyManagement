from django.forms import ModelForm

from core.models import Supplier, Buyer, Truck, TruckDriver


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ('name', 'company_name', 'email', 'phone')


class BuyerForm(ModelForm):
    class Meta:
        model = Buyer
        fields = ('name', 'company_name', 'email', 'phone')


class TruckForm(ModelForm):
    class Meta:
        model = Truck
        fields = ('plat_number', 'license')


class TruckDriverForm(ModelForm):
    class Meta:
        model = TruckDriver
        fields = ('first_name', 'last_name', 'phone')
