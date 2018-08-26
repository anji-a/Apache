from MM.models import MPM_element



def getElementTypes(request):
    """
    Used to get distinct types from the table
    :return:
    """
    element_types = []
    distinct_types = MPM_element.objects.distinct('element_type').values('element_type')

    for element in list(distinct_types):
        element_types.append(element['element_type'])

    return element_types