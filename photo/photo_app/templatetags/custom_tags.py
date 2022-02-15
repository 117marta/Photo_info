from django import template


register = template.Library()

@register.simple_tag
def division_decimal(val_1, val_2, val_3=3):
    try:
        division = int(val_1) / int(val_2)
    except Exception:
        return None
    result = f'{division:.{val_3}f}'
    return result
