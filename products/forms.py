from django.forms import ModelForm

from products.models import Item, ItemPackaging


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('title',)


class ItemPackagingForm(ModelForm):
    class Meta:
        model = ItemPackaging
        fields = ('title',)
