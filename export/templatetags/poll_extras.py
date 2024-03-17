from django.template import Library

register = Library()


@register.filter(name="toman")
def toman(value):
    return "{:,} تومان".format(int(value))
