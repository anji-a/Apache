from django import template
register = template.Library()

@register.simple_tag(takes_context=True)
def define(context,val=None):
    print("Define", val,type(val))
    return val.get('key','')