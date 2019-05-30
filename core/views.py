from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, CreateView

from core.forms import SupplierForm, BuyerForm, TruckForm, TruckDriverForm
from core.models import Supplier, Buyer, TruckDriver, Truck


class SupplierListView(ListView):
    model = Supplier
    paginate_by = 100
    context_object_name = 'suppliers'
    template_name = 'suppliers.html'


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context


class BuyerListView(ListView):
    model = Buyer
    paginate_by = 100
    context_object_name = 'buyers'
    template_name = 'buyers.html'


class TruckDriverListView(ListView):
    model = TruckDriver
    paginate_by = 100
    context_object_name = 'truck_drivers'
    template_name = 'truck_drivers.html'


class TruckListView(ListView):
    model = Truck
    paginate_by = 100
    context_object_name = 'trucks'
    template_name = 'truks.html'


class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'supplier_add.html'

    def get_success_url(self):
        return reverse('suppliers')


class BuyerCreateView(LoginRequiredMixin, CreateView):
    model = Buyer
    form_class = BuyerForm
    template_name = 'buyer_add.html'

    def get_success_url(self):
        return reverse('buyers')


class TruckCreateView(LoginRequiredMixin, CreateView):
    model = Truck
    form_class = TruckForm
    template_name = 'truck_add.html'

    def get_success_url(self):
        return reverse('trucks')


class TruckDriverCreateView(LoginRequiredMixin, CreateView):
    model = TruckDriver
    form_class = TruckDriverForm
    template_name = 'truck_driver_add.html'

    def get_success_url(self):
        return reverse('truck-drivers')
