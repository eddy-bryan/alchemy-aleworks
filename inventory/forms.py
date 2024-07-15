from django import forms
from .widgets import CustomClearableFileInput
from .models import Beer, MerchItem

class BeerForm(forms.ModelForm):
    """
    Form for creating or updating a Beer object.

    This form is used to add or edit a Beer object in the system. It inherits from
    Django's ModelForm and includes customizations for the 'image' field to use
    CustomClearableFileInput widget and apply a custom CSS class to form inputs.

    Attributes:
        image: ImageField for uploading beer images.
    """
    class Meta:
        model = Beer
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    
    def __init__(self, *args, **kwargs):
        """
        Initialise the form with custom attributes.

        Applies 'add-beer-form-input' CSS class to all form inputs for consistent styling.
        """
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'add-beer-form-input'

class MerchItemForm(forms.ModelForm):
    """
    Form for creating or updating a MerchItem object.

    This form is used to add or edit a MerchItem object in the system. It inherits from
    Django's ModelForm and includes customizations for the 'image' field to use
    CustomClearableFileInput widget and apply a custom CSS class to form inputs.

    Attributes:
        image: ImageField for uploading merchandise item images.
    """
    class Meta:
        model = MerchItem
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    
    def __init__(self, *args, **kwargs):
        """
        Initialise the form with custom attributes.

        Applies 'add-merch-form-input' CSS class to all form inputs for consistent styling.
        """
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'add-merch-form-input'