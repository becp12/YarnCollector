from django.forms import ModelForm
from .models import Quantity

class QuantityForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs.update({'min': '0'})
        self.fields['time'].widget.attrs.update({'type': 'time'})

    class Meta:
        model = Quantity
        fields = ['date', 'time', 'amount', 'unit']
        # time = forms.TimeInput(attrs={'type': 'time'})
    
