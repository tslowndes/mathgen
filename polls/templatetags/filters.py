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
def multiple(d,key):
    d = int(d[1:])
    print(int(key))
    if (d%int(key))==0:
        return 1
    else:
        return 0

@register.filter
def get_font_size(d,key):
    d = str(d)
    max_len = 100
    len_d = len(d)
    if len_d > max_len:
        len_d = max_len

    return "font-size:" + str(30 + (4*((max_len-len_d)/max_len))) +"px;"

@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)
