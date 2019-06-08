from django.forms import ModelForm

from invoices.models import Invoice


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        exclude = ('is_active',)

    def __init__(self, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'au-input au-input--full'})
