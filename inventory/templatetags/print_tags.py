from django import template

register = template.Library()


@register.simple_tag
def print_span(format_string):
    print("hello ", format_string)
    return format_string
