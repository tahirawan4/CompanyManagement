from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, CreateView, TemplateView

from core.forms import SupplierForm, BuyerForm, TruckForm, TruckDriverForm
from core.models import Supplier, Buyer, TruckDriver, Truck
from invoices.forms import InvoiceForm
from invoices.models import Invoice
from products.models import Item


class InvoiceListView(ListView):
    model = Invoice
    paginate_by = 100
    context_object_name = 'invoices'
    template_name = 'invoices.html'


class InvoiceCreateView(LoginRequiredMixin, CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'common-add-form.html'

    def get_success_url(self):
        return reverse('invoices')
