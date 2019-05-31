from django.forms import ModelForm

from core.models import Supplier, Buyer, Truck, TruckDriver


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ('name', 'company_name', 'email', 'phone')

    def __init__(self, *args, **kwargs):
        super(SupplierForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'au-input au-input--full'})


class BuyerForm(ModelForm):
    class Meta:
        model = Buyer
        fields = ('name', 'company_name', 'email', 'phone')

    def __init__(self, *args, **kwargs):
        super(BuyerForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'au-input au-input--full'})


class TruckForm(ModelForm):
    class Meta:
        model = Truck
        fields = ('plat_number', 'license')

    def __init__(self, *args, **kwargs):
        super(TruckForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'au-input au-input--full'})


class TruckDriverForm(ModelForm):
    class Meta:
        model = TruckDriver
        fields = ('first_name', 'last_name', 'phone')

    def __init__(self, *args, **kwargs):
        super(TruckDriverForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'au-input au-input--full'})
