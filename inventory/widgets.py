from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    A custom clearable file input widget for handling file uploads with additional customisations.

    Attributes:
        clear_checkbox_label (str): Label for the clear checkbox (default: 'Remove').
        initial_text (str): Label for the initial text (default: 'Current Image').
        input_text (str): Label for the input text (default: '').
        template_name (str): Path to the custom template used to render the widget
                             (default: 'inventory/custom_widget_templates/custom_clearable_file_input.html').

    Derived from the Boutique Ado project.
    """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'inventory/custom_widget_templates/custom_clearable_file_input.html'
