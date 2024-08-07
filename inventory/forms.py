from django import forms
from .models import Beer, MerchItem


class BeerForm(forms.ModelForm):
    """
    Form for creating or updating a Beer object.

    This form is used to add or edit a Beer object in the system. It
    inherits from Django's ModelForm and includes customisations for all
    fields except the 'image' field, which is excluded due to being
    replaced by an 'image_url' field.

    Attributes:
        image: ImageField for uploading beer images.
    """
    class Meta:
        model = Beer
        fields = '__all__'
        exclude = ['image']

    def __init__(self, *args, **kwargs):
        """
        Initialise the form with custom attributes.

        Applies 'add-beer-form-input' CSS class to all form inputs for
        consistent styling.
        """
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'add-beer-form-input'


class MerchItemForm(forms.ModelForm):
    """
    Form for creating or updating a MerchItem object.

    This form is used to add or edit a MerchItem object in the system. It
    inherits from Django's ModelForm and includes customisations for all
    fields except the 'image' field, which is excluded due to being
    replaced by an 'image_url' field.

    Attributes:
        image: ImageField for uploading merchandise item images.
    """
    class Meta:
        model = MerchItem
        fields = '__all__'
        exclude = ['image']

    def __init__(self, *args, **kwargs):
        """
        Initialise the form with custom attributes.

        Applies 'add-merch-form-input' CSS class to all form inputs for
        consistent styling.
        """
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'add-merch-form-input'
