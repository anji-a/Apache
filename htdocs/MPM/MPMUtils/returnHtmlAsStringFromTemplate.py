from django.template.loader import render_to_string

def returnHtmlAsStringFromTemplate(*args,**kwargs):
    templateName = kwargs['templateName']
    templateDate = kwargs['templateData']

    return render_to_string(templateName, templateDate)