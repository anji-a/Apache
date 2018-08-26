from MM.models import MPM_element
from django.template.loader import render_to_string

def getElementData(request):
    """
            This function will return the element data
            :param request:
            :return:
            """
    element_name = request.get('element_name')
    ele_obj = MPM_element.objects.filter(element_displayname=element_name,element_mode='Development').values('element_displayname', 'element_stream','element_type')
    #print(ele_obj[0].get('element_stream'))
    #resdata = {"html": render_to_string(ele_obj[0].get('element_stream'), request), 'responseData': request}
    request['element_type'] = ele_obj[0].get('element_type')
    request['element_stream'] = ele_obj[0].get('element_stream')
    resdata = {"html":render_to_string('MM/openElement.html', request), 'responseData': request}
    return resdata