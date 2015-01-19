# -*- coding: utf-8 -*-
from django import template
from django.template.loader import get_template
from django.template import Context
from main.helper.constants import constants

register = template.Library()

@register.simple_tag
def main_global_js_var() :
    return '<script> main = {}; </script>'

@register.inclusion_tag('helper/js_constants.html')
def js_constants() :
    context = {
        'constants': constants,
    }
    return context

