from django import forms
from .widgets import CustomClearableFileInput
from .models import Beer, MerchItem

class BeerForm(forms.ModelForm):
    class Meta:
        model = Beer
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'add-beer-form-input'

class MerchItemForm(forms.ModelForm):
    class Meta:
        model = MerchItem
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'add-merch-form-input'