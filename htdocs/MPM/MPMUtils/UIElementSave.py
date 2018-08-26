import datetime,sys
from MPMUtils.ElementDBSave import ElementDBSave
from MPMUtils.ElementFileSaveOrUpdate import ElementFileSaveOrUpdate
from MPMUtils.parseHtml import parseHtml
from MPMUtils.Logging import logError


def UIElementSave(request):
    """
            Used to save the UI Screen
            :param request:
            :return:
            """
    try:
        # print(request)
        # print(request.POST['element_dev_stream'])
        # web_page = WebPage.objects.get_or_create(topic=top, url=fakeurl, name=fake_name)[0]
        # Setup defaults
        element = {}
        element['element_name'] = request.get('element_name')
        element['element_createddatetime'] = datetime.datetime.now()
        element['element_updatedatetime'] = datetime.datetime.now()
        element['element_stream'] = request.get('element_stream')
        #element['element_stream'] = parseHtml(request.get('element_stream'), "Save")
        element['element_displayname'] = request.get('element_name')
        element['element_mode'] = "Development"
        element['element_type'] = request.get('element_type')

        status = ElementDBSave(element, request)
        if status == "DBSucess":
            fileSatatus = ElementFileSaveOrUpdate(element,request)

            if fileSatatus == "Element Files save Sucess":
                return "File Save Sucess"
            else:
                return "File Save Failed"
            return "Save Sucess"
        else:
            return "DBFail"

    except:
        logError(log=sys.exc_info())
        return "Save failed"