from django import template
from django.template import Node

register = template.Library()


@register.filter
def first_words(value, n):

    return " ".join(value.split()[:n]) + "..."


@register.tag
def lineless(parser, token):
    nodelist = parser.parse(("endlineless",))
    parser.delete_first_token()
    return LinelessNode(nodelist)


class LinelessNode(Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        input_str = self.nodelist.render(context)
        output_str = ""
        for line in input_str.splitlines():
            if line.strip():
                output_str = "\n".join((output_str, line))
        return output_str
