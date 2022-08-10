from django.forms import ModelForm
from .models import Quantity

class QuantityForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs.update({'min': '0'})

    class Meta:
        model = Quantity
        fields = ['date', 'amount', 'unit']
    
