# -*- coding: utf-8 -*-
from django import template
from django.core.urlresolvers import reverse

register = template.Library()
@register.inclusion_tag('account/auth_menu.html', takes_context = True)
def auth_menu(context):
    request = context.get('request', None)
    if request:
        items = []
        prefix = ''
        auth_status = request.user.is_authenticated()
        if auth_status:
            prefix = u'Вошли как %s' % request.user.get_short_name()
            items.append({
                'url': reverse('account:logout'),
                'title': u'Выйти',
            })
        else:
            items.append({
                'url': reverse('account:login'),
                'title': u'Войти',
            })

        return {
            'prefix': prefix,
            'items': items,
        }

