from django.forms import ModelForm, Form
from .models import EntryItem

class EntryItemForm(ModelForm):

    class Meta:
        model = EntryItem
        fields = ("keyword",)