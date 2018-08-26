from MPMUtils.parseHtml import parseHtml
import os


def UI_Preview(request):
    parsehtml = parseHtml(request.get('element_stream', ''), 'Preview')
    rootdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tempplatespath = os.path.join(os.path.join(rootdir, "templates"), "MM")
    filename = request.get('element_name', '') + "_Preview"
    filePath = os.path.join(tempplatespath, filename + ".html")

    f = open(filePath, "w+")
    f.write(parsehtml)
    f.close()

    return filename