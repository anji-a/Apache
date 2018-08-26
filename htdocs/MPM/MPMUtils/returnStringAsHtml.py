from django.utils.html import format_html
from django.utils.safestring import mark_safe

def returnStringAsHtml(html):
    #print(html)
    return mark_safe(html)