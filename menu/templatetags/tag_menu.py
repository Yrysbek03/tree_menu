import re

from django import template
from django.shortcuts import get_object_or_404
from menu.models import Menu
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu = get_object_or_404(Menu, name=menu_name, parent=None)
    l_context = {'menu_item': menu}
    m_id = -1
    match = re.findall(r"/(.*?)/", context['request'].path)
    if match:
        m_id = match[-1]
    try:
        dm_item = Menu.objects.get(pk=m_id)
    except ObjectDoesNotExist:
        pass
    else:
        dm_ids = dm_item.get_parents_ids() + [dm_item.id]
        l_context['dm_ids'] = dm_ids
    return l_context

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu_item_children(context, menu_item_id):
    menu_item = get_object_or_404(Menu, pk=menu_item_id)
    l_context = {'menu_item': menu_item}
    if 'dm_ids' in context:
        l_context['dm_ids'] = context['dm_ids']
    return l_context