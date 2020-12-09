from django import template

register = template.Library()

@register.filter
def lookup(d, key):
    return d[key]

@register.filter
def add(d, key):
    return int(d) + int(key)

@register.filter
def set(d, key):
    d = key
    return int(key)