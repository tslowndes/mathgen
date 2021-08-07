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

@register.filter
def first_char(d,key):
    return d[0]

@register.filter
def get_font_size(d,key):
    d = str(d)
    max_len = 100
    len_d = len(d)
    if len_d > max_len:
        len_d = max_len

    return "font-size:" + str(3 + (2*((max_len-len_d)/max_len))) +"vh;"