import subprocess

from django import template

register = template.Library()


@register.simple_tag
def print_span(format_string):
    print("hello ", format_string)
    return format_string


@register.simple_tag
def get_app_version():
    label = subprocess.check_output(["git", "describe", "--first-parent"])
    return label


@register.simple_tag
def img_tag_url():
    pass
