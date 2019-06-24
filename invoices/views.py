from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, DeleteView

from core.forms import SupplierForm, BuyerForm, TruckForm, TruckDriverForm
from core.models import Supplier, Buyer, TruckDriver, Truck
from invoices.forms import InvoiceForm
from invoices.models import Invoice, OrderItem
from products.models import Item, ItemPackaging


class InvoiceListView(ListView):
    model = Invoice
    paginate_by = 100
    context_object_name = 'invoices'
    template_name = 'invoices.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_year = self.request.GET.get('year')
        years_list = [str(datetime.now().date().year - i) for i in range(0, 10)]
        context['years_list'] = years_list
        context['selected_year'] = selected_year
        if selected_year:
            invoices_data = context['invoices']
            context['invoices'] = Invoice.objects.filter(created_at__year=selected_year,
                                                         id__in=invoices_data.values_list('id', flat=True))
        return context


class InvoiceCreateView(LoginRequiredMixin, TemplateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice_form.html'

    def get_context_data(self, **kwargs):
        kwargs['buyers'] = Buyer.objects.all()
        kwargs['suppliers'] = Supplier.objects.all()
        kwargs['items'] = Item.objects.all()
        kwargs['packagings'] = ItemPackaging.objects.all()
        kwargs['trucks'] = Truck.objects.all()
        kwargs['truck_drivers'] = TruckDriver.objects.all()

        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        buyer_id = request.POST.get('buyer')
        supplier_id = request.POST.get('supplier')
        truck_driver_id = request.POST.get('truck_driver')
        truck_id = request.POST.get('truck')
        pickup_place = request.POST.get('pickup_place')
        delivery_location = request.POST.get('delivery_location')
        date_pickup = request.POST.get('date_pickup')
        items = request.POST.getlist('item[]')
        item_pack = request.POST.getlist('itempack[]')
        quantity = request.POST.getlist('quantity[]')
        invoice = Invoice.objects.create(supplier_id=supplier_id, buyer_id=buyer_id, truck_driver_id=truck_driver_id,
                                         truck_id=truck_id, place_of_pickup=pickup_place,
                                         place_of_deliver=delivery_location,
                                         date_pick_up=date_pickup)
        for index, elem in enumerate(items):
            item_id = items[index]
            item_pack_id = item_pack[index]
            item_quantity = quantity[index]
            order_item = OrderItem.objects.create(item_id=item_id, item_packaging_id=item_pack_id,
                                                  quantity=item_quantity)
            invoice.order_items.add(order_item)

        return redirect(reverse('invoices'))


class InvoiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Invoice
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('invoices')
