from MM.models import MPM_element


def getListofElementsbasedonType(request):
    """
            used to get the list of items based on type
            :return:
            """
    element_type = request.get('element_type')
    elements = []

    ele_obj = MPM_element.objects.filter(element_type=element_type, element_mode="Development").values(
        'element_displayname')

    for element in list(ele_obj):
        elements.append(element['element_displayname'])

    return elements