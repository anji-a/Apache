from MPMUtils import returnStringAsHtml,returnHtmlAsStringFromTemplate

def TestTag6(data):
    print(data.get('Tagdata'))
    return returnStringAsHtml.format_html(
        returnHtmlAsStringFromTemplate.returnHtmlAsStringFromTemplate(
            templateName='MM/TestTag6.html', templateData=data.get('Tagdata')))