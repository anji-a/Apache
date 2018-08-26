from MPMUtils.returnStringAsHtml import returnStringAsHtml
from MPMUtils.exeCode import exeCode
from MPMUtils.returnHtmlAsStringFromTemplate import returnHtmlAsStringFromTemplate
from django.shortcuts import render

def testDropdown(data):

    #print("testDropdown Method", data.get('Tagdata'))
    tagdata = {}
    tagdata = data.get('Tagdata')
    #print(tagdata)
    tagdata['fun_name'] = tagdata.get('DropDown_property_value')

    #print("testDropdown Method", tagdata)
    responseData = exeCode(data=tagdata)
    responseData['key'] = 'key'
    responseData['value'] = 'value'
    responseData['property_name'] = 'test'
    #print("testDropdown Method", responseData)
    return returnStringAsHtml(returnHtmlAsStringFromTemplate(templateName='MM/testDropdown.html', templateData=responseData))
    #return render('', 'MM/testDropdown.html', context=responseData)