from django.utils import timezone
from django.views.generic.list import ListView

from products.models import Item, ItemPackaging


class ItemsListView(ListView):
    model = Item
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ItemPackagingListView(ListView):
    model = ItemPackaging
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
