from bs4 import BeautifulSoup
import json,sys
from MPMUtils.Logging import logError

def parseHtml(html,action):
    """
            Used to parse HTML
            :param html:
            :return:
            """
    soup = BeautifulSoup(html, "lxml")
    generatedhtl = ''
    # print(soup)

    for tag in soup.find_all(attrs={"data-edit": "remove"}):
        tag.decompose()

    for tag in soup.find_all(attrs={"data-edit": "merge"}):
        tag.unwrap()

    for tag in soup.find_all(attrs={"data-edit": "regenerate"}):
        data_controlset = json.loads(tag['data-controlset'])

        # print(".......................",data_controlset.get('layout_class','Hello'))
        if data_controlset.get("controlType", '') == "label":
            #print(data_controlset)
            new_col_tag = soup.new_tag("div")
            new_col_tag['class'] = data_controlset.get("column_class", '')
            new_col_tag['style'] = data_controlset.get("column_style", '')
            new_label_tag = soup.new_tag("label")
            new_label_tag.string = "{{ " + data_controlset.get("label_property_property", '') + " }}"
            new_label_tag['class'] = data_controlset.get("label_property_class", '')
            new_label_tag['style'] = data_controlset.get("label_property_style", '')
            # new_label_tag.string='{% include "MM/UIOptions.html" %}'
            new_col_tag.append(new_label_tag)
            tag.replace_with(new_col_tag)

        if data_controlset.get("controlType", '') == "input":
            new_col_tag = soup.new_tag("div")
            new_col_tag['class'] = data_controlset.get("column_class", '')
            new_col_tag['style'] = data_controlset.get("column_style", '')
            new_label_tag = soup.new_tag("label")
            new_label_tag.string = "{{ " + data_controlset.get("input_property_label", '') + " }}"
            new_label_tag['for'] = data_controlset.get("input_property_property", '')
            new_label_tag['class'] = data_controlset.get("label_property_class", '')
            new_label_tag['style'] = data_controlset.get("label_property_style", '')
            new_input_tag = soup.new_tag("input")
            new_input_tag['name'] = data_controlset.get("input_property_property", '')
            new_input_tag['class'] = data_controlset.get("property_property_class", '')
            new_input_tag['style'] = data_controlset.get("property_property_style", '')
            new_input_tag['value'] = "{{" + data_controlset.get("input_property_property", '') + "}}"
            new_label_tag.append(new_input_tag)
            new_col_tag.append(new_label_tag)
            tag.replace_with(new_col_tag)

        if data_controlset.get("controlType", '') == "button":
            new_col_tag = soup.new_tag("div")
            new_col_tag['class'] = data_controlset.get("column_class", '')
            new_col_tag['style'] = data_controlset.get("column_style", '')
            new_input_tag = soup.new_tag("input")
            new_input_tag['type'] = "button"
            new_input_tag['value'] = data_controlset.get("button_property_value", '')
            new_input_tag['class'] = data_controlset.get("button_property_class", '')
            new_input_tag['style'] = data_controlset.get("button_property_style", '')
            new_input_tag['onclick'] = data_controlset.get("button_property_click", '')
            new_col_tag.append(new_input_tag)
            tag.replace_with(new_col_tag)

        if data_controlset.get("controlType", '') == "dropdown":
            new_col_tag = soup.new_tag("div")
            new_col_tag['class'] = data_controlset.get("column_class", '')
            new_col_tag['style'] = data_controlset.get("column_style", '')
            #tag_data = {"choices": ["First choice", "second choice", "6th choice"]}
            tag_data = data_controlset
            new_col_tag.string = "{% load Tagutility %}{% TagUtility context fun_name='testDropdown' Tagdata='"+json.dumps(tag_data)+"'%}"
            tag.replace_with(new_col_tag)

        if data_controlset.get("controlType", '') == "layout":
            tag['class'] = data_controlset.get("layout_class", '')
            tag['style'] = data_controlset.get("layout_style", '')

        if data_controlset.get("controlType", '') == "emptycontol":
            new_col_tag = soup.new_tag("div")
            new_col_tag['class'] = data_controlset.get("column_class", '')
            new_col_tag['style'] = "height:20px;" + data_controlset.get("column_style", '')
            # new_span_tag = soup.new_tag("span")
            # new_span_tag['style'] = "height:20px"
            # new_col_tag.append(new_span_tag)
            tag.replace_with(new_col_tag)

    if action == "Preview":
        try:
            """ReviewfilePath = MM_Utiliy.getTeplatePath(MM_Utiliy, "UIPreview_MPM")
            rf = open(ReviewfilePath, "r+")
            phtml = rf.read()

            Psoup = BeautifulSoup(phtml, "lxml")

            ptag = Psoup.find_all(id="previewID")
            new_tag=soup.new_tag("div")
            new_tag['id']='previewID'
            #print(soup.prettify())
            new_tag.append(soup)


            for el in ptag:
                el.replace_with(new_tag)

            rf.seek(0)
            rf.write(Psoup.prettify())
            rf.close()"""

            Psoup = BeautifulSoup(soup.prettify(formatter="html"), 'lxml')
            htmlTag = Psoup.body
            headTag = Psoup.new_tag("head")
            linkTag1 = Psoup.new_tag("link")
            linkTag1['href'] = "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
            linkTag1['rel'] = 'stylesheet'
            linkTag2 = Psoup.new_tag("link")
            linkTag2['href'] = "static/css/Portal.css"
            linkTag2['rel'] = 'stylesheet'
            linkTag3 = Psoup.new_tag("link")
            linkTag3['href'] = "//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css"
            linkTag3['rel'] = 'stylesheet'
            scriptTag = Psoup.new_tag("script")
            scriptTag['src'] = "https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"
            scriptTag2 = Psoup.new_tag("script")
            scriptTag2['src'] = "https://code.jquery.com/ui/1.12.1/jquery-ui.js"
            scriptTag3 = Psoup.new_tag("script")
            scriptTag3['src'] = "static/js/tabs.js"
            scriptTag4 = Psoup.new_tag("script")
            scriptTag4['src'] = "static/js/app.js"
            scriptTag5 = Psoup.new_tag("script")
            scriptTag5['src'] = "static/js/Portal.js"

            headTag.append(linkTag1)
            headTag.append(linkTag2)
            headTag.append(linkTag3)
            headTag.append(scriptTag)
            headTag.append(scriptTag2)
            headTag.append(scriptTag3)
            headTag.append(scriptTag4)
            headTag.append(scriptTag5)
            # headTag.wrap(' <head><meta charset="utf-8"/><title>Preview</title><link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet"/><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script><script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script><script src="static/js/Portal.js" type="text/javascript"></script><link href="static/css/Portal.css" rel="stylesheet"/></head>')
            htmlTag.insert_before(headTag)
            #print(Psoup)
            return Psoup.prettify(formatter="html")
        except:

            logError(log=sys.exc_info())

    return soup.prettify(formatter="html")