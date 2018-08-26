from bs4 import BeautifulSoup
import json,sys
from MPMUtils.Logging import logError



def parseForm(request):
    try:

        # print("Parse Form",request)
        soup = BeautifulSoup("<html><form></form></html>", "lxml")
        new_form_tag = soup.new_tag("form")
        new_form_tag['method'] = request.get('method', 'POST')
        new_form_tag['action'] = "/" + request.get('action', '')
        new_form_tag['id'] = request.get('element_name', '')
        hideEle = [k for k in request.keys() if k.startswith('hide_')]
        for v in hideEle:
            new_input_tag = soup.new_tag("input")
            new_input_tag['name'] = request.get(v, '')
            new_input_tag['value'] = "{{" + request.get(v, '') + "}}"
            new_input_tag['type'] = "hidden"
            new_form_tag.append(new_input_tag)

        new_div_tag = soup.new_tag("div")
        new_form_tag.append(new_div_tag)
        new_div_tag.string = '{% include "MM/' + request.get('includeElement', '') + '.html" %}'
        # includeElement
        new_script_tag = soup.new_tag("script")
        new_script_tag.string = "$(document).on('submit','#" + request.get('element_name', '') + "',function(e){\n" \
                                                                                                 "    e.preventDefault();\n" \
                                                                                                 "$.ajax({ data: $(this).serialize(),\n" \
                                                                                                 "type: $(this).attr('method'),\n" \
                                                                                                 "url: $(this).attr('action'),\n" \
                                                                                                 "success: function(response) {\n" \
                                                                                                 "var controlData = JSON.parse(response.responseData.response);\n" \
                                                                                                 "console.log(controlData);\n" \
                                                                                                 "$('#" + request.get(
            'element_name', '') + "').html(response.html);\n" \
                                  "//console.log(response.responseData.controlType);\n" \
                                  "$('#'+controlData.id).attr('data-controlset',response.responseData.response);\n" \
                                  "$('#'+controlData.id).attr('class',controlData.column_class);\n" \
                                  "$('#'+controlData.id).attr('style',controlData.column_style);\n" \
                                  "if(response['success']) {\n" \
                                  "}\n" \
                                  "if(response['error']) {\n" \
                                  "}\n" \
                                  "},\n" \
                                  "error: function (request, status, error) {\n" \
                                  "console.log(request.responseText);\n" \
                                  "}\n" \
                                  "});\n" \
                                  "});\n"

        formtag = soup.form
        formtag.replace_with(new_form_tag)

        htmltag = soup.html
        htmltag.insert_after(new_script_tag)
        #print("new Form", new_form_tag)
        print("form tag", soup.prettify(formatter="html"))
        # foodict = [k for k in request.keys() if k.startswith('hide_')]
        # print("Pares From", foodict)
        return soup.prettify(formatter="html")
    except:
        logError(log=sys.exc_info())

    return True;
