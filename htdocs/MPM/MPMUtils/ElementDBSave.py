import datetime
import sys
import os
from MM.models import MPM_element
from MPMUtils.returnHtmlAsStringFromTemplate import returnHtmlAsStringFromTemplate
from MPMUtils.Logging import logError
from MPMUtils.parseHtml import parseHtml
from MPMUtils.parseForm import parseForm


def ElementDBSave(element,request):
    try:
        #print(request)
        if request.get('element_type') == "Section":

            ElementObject = MPM_element.objects.get_or_create(element_name=element['element_name'], defaults=element)[0]
            ElementObject.element_updatedatetime = datetime.datetime.now()
            if (ElementObject.element_createddatetime == ""):
                ElementObject.element_createddatetime = datetime.datetime.now()

            ElementObject.element_stream = parseHtml(request.get('element_stream'), "Save")
            ElementObject.element_displayname = element['element_name']
            ElementObject.element_mode = "Original"
            ElementObject.element_type = element['element_type']

            ElementObject.save()

        elif request.get('element_type') == "Tag":
            element['element_name'] = request.get('element_name') + "_py"
            ElementObject = MPM_element.objects.get_or_create(element_name=element['element_name'], defaults=element)[0]
            ElementObject.element_updatedatetime = datetime.datetime.now()
            if (ElementObject.element_createddatetime == ""):
                ElementObject.element_createddatetime = datetime.datetime.now()

            ElementObject.element_stream = request.get(element['element_name'])
            ElementObject.element_displayname = element['element_name']
            ElementObject.element_mode = "Original"
            ElementObject.element_type = element['element_type']
            ElementObject.save()

            element['element_name'] = request.get('element_name') + "_html"
            ElementObject = MPM_element.objects.get_or_create(element_name=element['element_name'], defaults=element)[0]
            ElementObject.element_updatedatetime = datetime.datetime.now()
            if (ElementObject.element_createddatetime == ""):
                ElementObject.element_createddatetime = datetime.datetime.now()

            ElementObject.element_stream = request.get(element['element_name'])
            ElementObject.element_displayname = element['element_name']
            ElementObject.element_mode = "Original"
            ElementObject.element_type = element['element_type']
            ElementObject.save()

        elif request.get('element_type') == "Form":

            ElementObject = MPM_element.objects.get_or_create(element_name=element['element_name'], defaults=element)[0]
            ElementObject.element_updatedatetime = datetime.datetime.now()
            if (ElementObject.element_createddatetime == ""):
                ElementObject.element_createddatetime = datetime.datetime.now()

            ElementObject.element_stream = parseForm(request)
            ElementObject.element_displayname = element['element_name']
            ElementObject.element_mode = "Original"
            ElementObject.element_type = element['element_type']

            ElementObject.save()
            rootdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            tempplatespath = os.path.join(os.path.join(rootdir, "templates"), "MM")
            filePath = os.path.join(tempplatespath, request.get('element_name') + ".html")

            f = open(filePath, "w+")
            f.write(ElementObject.element_stream)
            f.close()
            hideEle = {k: v for k, v in request.items() if k.startswith('hide_')}

            request['hideEle'] = hideEle

            request['element_stream'] = returnHtmlAsStringFromTemplate(templateName='MM/NewFormWorkAreawithoutheader.html',templateData=request)
            print("DB save", request.get('element_stream'))

        element['element_name'] = request.get('element_name') + "_Dev"
        ElementObject = MPM_element.objects.get_or_create(element_name=element['element_name'], defaults=element)[0]
        ElementObject.element_updatedatetime = datetime.datetime.now()
        if (ElementObject.element_createddatetime == ""):
            ElementObject.element_createddatetime = datetime.datetime.now()

        ElementObject.element_stream = request.get('element_stream')
        ElementObject.element_displayname = request.get('element_name')
        ElementObject.element_mode = "Development"
        ElementObject.element_type = element['element_type']

        ElementObject.save()
        return "DBSucess"

    except:
        logError(log=sys.exc_info())
        return "DBFail"