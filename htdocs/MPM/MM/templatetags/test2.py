from django import template
from MPMUtils import returnStringAsHtml,returnHtmlAsStringFromTemplate

register = template.Library()

tag = 'MM/Hello.html'

@register.inclusion_tag(tag)
def show_results2(poll):
    #choices = poll.choice_set.all()
    #globals().tag = 'MM/Hello.html'
    print(poll,"Hello")
    return {'choices': ['First choice', 'second choice', 'third choice']}

def show_results1(data):

    #choices = poll.choice_set.all()
    #print(globals())
    globals()[tag] = 'MM/login.html'
    #print(globals())
    #globals().tag = 'MM/Hello.html'
    #from django.template.loader import get_template
    #t = get_template('MM/Hello.html')
    #register.inclusion_tag(t)(show_results1)
    #register.tag('show',show_results2)
    #from django.core.cache import cache
    #print(cache.get('test2'),"Hello")
    #print(cache.clear())
    return returnStringAsHtml.format_html(returnHtmlAsStringFromTemplate.returnHtmlAsStringFromTemplate(templateName='MM/Hello.html', templateData=data))


@register.inclusion_tag('MM/Hello.html')
def show_results3(poll):
    #choices = poll.choice_set.all()
    print(poll,"Hello")
    return {'choices': ['First choice', 'second choice', '3rd choice']}


def test2(data):
    print(data.get('Tagdata'))
    return returnStringAsHtml.format_html(
        returnHtmlAsStringFromTemplate.returnHtmlAsStringFromTemplate(templateName='MM/Hello.html', templateData=data.get('Tagdata')))