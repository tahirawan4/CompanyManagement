from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from products.forms import ItemForm, ItemPackagingForm
from products.models import Item, ItemPackaging


class ItemsListView(LoginRequiredMixin, ListView):
    model = Item
    paginate_by = 100
    template_name = 'items.html'
    context_object_name = 'items'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context


class ItemPackagingListView(LoginRequiredMixin, ListView):
    model = ItemPackaging
    paginate_by = 100
    template_name = 'item_packaging.html'
    context_object_name = 'packagings'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'common-add-form.html'

    def get_success_url(self):
        return reverse('items')


class ItemPackagingCreateView(LoginRequiredMixin, CreateView):
    model = ItemPackaging
    form_class = ItemPackagingForm
    template_name = 'common-add-form.html'

    def get_success_url(self):
        return reverse('item-packaging')


class ItemPackagingUpdateView(LoginRequiredMixin, UpdateView):
    model = ItemPackaging
    form_class = ItemPackagingForm
    template_name = 'common-add-form.html'

    def get_success_url(self):
        return reverse('item-packaging')


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'common-add-form.html'

    def get_success_url(self):
        return reverse('items')


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('items')


class ItemPackagingDeleteView(LoginRequiredMixin, DeleteView):
    model = ItemPackaging
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('item-packaging')
