from django import template
from django.template import Template
from django.template.loader import render_to_string
import json
from django.utils.html import format_html,escape
from django.utils.safestring import mark_safe
from django.http import HttpResponse,HttpRequest
from . import test2
from MPMUtils.exeCode import exeCode
register = template.Library()


@register.simple_tag(takes_context=True)
def TagUtility(context,  *args, **kwargs):
    #print(kwargs)
    #print(context)
    #responseData = getattr(test2, "show_results1")("hi")
    #exec("from . import test2",globals())
    #globals()['show_results1']("hi")
    #exeCode(funname='name',data=kwargs)
    kwargs['context'] = context
    #kwargs['Tagdata'] = json.loads(kwargs.get('Tagdata'))
    #print(type(kwargs.get('Tagdata')))
    if type(kwargs.get('Tagdata')) is not type({}):
        #print("IN str")
        kwargs['Tagdata'] = json.loads(kwargs.get('Tagdata', '{}'))
    #data = {'choices': ['First choice', 'second choice', '3rd choice']}
    #resdata = {"html": render_to_string('MM/Hello.html', data), 'responseData': data}
    # return JsonResponse(resdata)
    return exeCode(data=kwargs)
    #return format_html(resdata['html'])
    #data = {'choices': ['First choice', 'second choice', 'third choice']}
    #return Template('MM/Hello.html').render(context)

