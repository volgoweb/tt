# -*- coding: utf-8 -*-
from django import template
from django.template.loader import get_template, render_to_string
from django.template import Context

from main.helper.constants import constants

register = template.Library()

#TODO с шаблонами все-таки удобнее чем с тегами, так что надо переделывать

def get_rendered_widget(field_type, widget, mode, *args, **kwargs):
    tpl_path = 'helper/field/field_{0}/widget_{1}/{2}_mode.html'.format(field_type, widget, mode)
    return render_to_string(tpl_path, kwargs)

@register.simple_tag
def choices_field_add_mode(widget, *args, **kwargs) :
    tpl_path = 'helper/field/field_choices/{0}/add_mode.html'.format(widget)
    return render_to_string(tpl_path, kwargs)

@register.simple_tag
def choices_field_edit_mode(widget, *args, **kwargs) :
    tpl_path = 'helper/field/field_choices/{0}/edit_mode.html'.format(widget)
    return render_to_string(tpl_path, kwargs)

@register.simple_tag
def choices_field_view_and_edit_mode(widget, *args, **kwargs) :
    tpl_path = 'helper/field/field_choices/{0}/view_and_edit_mode.html'.format(widget)
    return render_to_string(tpl_path, kwargs)

@register.simple_tag
def render_field(field_type, widget, mode, *args, **kwargs) :
    get_rendered_widget(field_type, widget, mode, *args, **kwargs)
