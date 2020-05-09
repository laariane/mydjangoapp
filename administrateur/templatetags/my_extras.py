from django import template

register = template.Library()
def lookup(value, key):
    return value[key]
