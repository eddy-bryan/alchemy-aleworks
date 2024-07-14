from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Custom Django template filter to calculate the subtotal of an item.

    Args:
    - price (Decimal): Price of the item.
    - quantity (int): Quantity of the item.

    Returns:
    - Decimal: Subtotal of the item (price * quantity).
    """
    return price * quantity
