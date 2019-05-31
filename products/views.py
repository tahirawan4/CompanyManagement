from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils import timezone
from django.views.generic import CreateView, TemplateView
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

        # def form_valid(self, form):
        #     post = TopicPosts.objects.filter(slug=self.kwargs.get('slug')).first()
        #     form.instance.topic_post_id = post.id
        #     form.instance.user = self.request.user
        #     return super().form_valid(form)
