from django import template
from ..models import *

register = template.Library()


@register.simple_tag()
def get_social_links():
    """Вывод ссылок соц сетей"""
    return Social.objects.all()
