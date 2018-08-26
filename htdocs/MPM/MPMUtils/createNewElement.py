from django.template.loader import render_to_string

def createNewElement(request):
    """
            Used to crate new Element
            :param request:
            :return:
            """
    requestData = request
    print(request)
    if request.get('element_type')=='Tag':
        resdata = {"html": render_to_string("MM/NewTagWorkArea.html", requestData), 'responseData': requestData}
    elif request.get('element_type')=='Form':
        resdata = {"html": render_to_string("MM/NewFormWorkArea.html", requestData), 'responseData': requestData}
    else:
        resdata = {"html": render_to_string("MM/NewHTMLWorkArea.html", requestData), 'responseData': requestData}
    # return JsonResponse(resdata)
    return resdata
