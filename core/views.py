from django.views.generic import ListView

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
    context_object_name = 'trucs'
    template_name = 'truks.html'
