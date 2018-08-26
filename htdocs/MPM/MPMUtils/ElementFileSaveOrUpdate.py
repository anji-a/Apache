import os,sys
from MPMUtils.Logging import logError
from MPMUtils.parseHtml import parseHtml


def ElementFileSaveOrUpdate(element,request):
    try:
        rootdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if request.get('element_type') == "Section":
            tempplatespath = os.path.join(os.path.join(rootdir, "templates"), "MM")
            filePath = os.path.join(tempplatespath, request.get('element_name') + ".html")

            f = open(filePath, "w+")
            f.write(parseHtml(request.get('element_stream'), "Save"))
            f.close()
        elif request.get('element_type') == "Tag":
            tempplatespath = os.path.join(os.path.join(rootdir, "templates"), "MM")
            filePath = os.path.join(tempplatespath, request.get('element_name') + ".html")

            f = open(filePath, "w+")
            f.write(request.get(request.get('element_name') + "_html"))
            f.close()

            tagpath = os.path.join(os.path.join(rootdir, "MM"), "templatetags")
            filePath = os.path.join(tagpath, request.get('element_name') + ".py")
            f = open(filePath, "w+")
            f.write(request.get(request.get('element_name') + "_py"))
            f.close()

        return "Element Files save Sucess"
    except:
        logError(log=sys.exc_info())
        return "Element Save Fail"