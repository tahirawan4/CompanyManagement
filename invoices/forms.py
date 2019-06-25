from django.forms import ModelForm

from invoices.models import Invoice, Year


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        exclude = ('is_active',)

    def __init__(self, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'au-input au-input--full'})


class YearForm(ModelForm):
    class Meta:
        model = Year
        fields = ('year',)

    def __init__(self, *args, **kwargs):
        super(YearForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'au-input au-input--full'})
