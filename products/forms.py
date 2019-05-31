from django.forms import ModelForm

from products.models import Item, ItemPackaging


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('title',)

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'au-input au-input--full'})



class ItemPackagingForm(ModelForm):
    class Meta:
        model = ItemPackaging
        fields = ('title',)

    def __init__(self, *args, **kwargs):
        super(ItemPackagingForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'au-input au-input--full'})

    #
    # def __init__(self, *args, **kwargs):
    #     super(ItemPackagingForm, self).__init__(*args, **kwargs)
    #     self.fields.
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'
