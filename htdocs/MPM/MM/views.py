import json
import sys
import traceback

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from MPMUtils.Logging import logError
from MPMUtils.exeCode import exeCode
from MPMUtils.DickUpdate import DickUpdate

# Create your views here.


def index(request):
    """
    Used for initial request
    :param request:
    :return:
    """
    my_dic = {
        'loginmessage': ''
    }

    return render(request, 'MM/login.html', context = my_dic)

@csrf_exempt
def loginApp(request):

    if request.method == 'POST' or request.method == 'GET':
        try:
            username = request.POST['username']
            password = request.POST['psw']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'MM/workspace.html', context={'user': user})

            else:
                return render(request, 'MM/login.html', context={'loginmessage': "Login not success Please try to re login"})
        except:
            logError(log=sys.exc_info())


    else:
        print("its get method")


def logoutapp(request):
    """
    Used to log out the user
    :param request:
    :return:
    """
    try:
        logout(request)
        return render(request, 'MM/login.html', context={'loginmessage': "Successfully logged out, Please login here"})
    except:
        logError(log=sys.exc_info())


@csrf_exempt
def standardFunc(request):
    if request.method == 'POST':

        print("Standard Function",request.POST)
        #function_name=request.POST['fun_name']
        #compile_code(message=post_id, repeat= Task.HOURLY)
        #responseData = getattr(MM_Utiliy,function_name)(MM_Utiliy,request)
        responseData = exeCode(data=request.POST.dict())
        dick = {
             'response': responseData
        }
        # likedpost = Post.obejcts.get(pk=post_id)  # getting the liked posts
        # m = Like(post=likedpost)  # Creating Like Object
        # m.save()  # saving it to store in database
        return HttpResponse(
            json.dumps(dick),
            content_type="application/json"
        )  # Sending an success response
    else:
        return HttpResponse("Request method is not a GET")


@csrf_exempt
def UIscreeninclude(request):
    """
    used to return UI screen
    :param request:
    :return:
    """
    if request.method == 'POST':
        if request.is_ajax():
            if 'id' in request.POST.dict():

                request.session = DickUpdate(request.POST.dict()['id'], request.session,
                                                       request.POST.dict())

                requestData = request.POST.dict()
                requestData['response']=json.dumps(request.session[request.POST['id']])
                print("UI Screen Include",requestData)
                resdata= {"html": render_to_string(request.POST['UIElement'], requestData),'responseData':requestData}
                #return JsonResponse(resdata)
                return HttpResponse(json.dumps(resdata), content_type='application/json')
            else:
                requestData = request.POST.dict()
                #requestData['test'] = {'hi':'Hello'}
                print("In Else Block",requestData)
                return render(request, request.POST['UIElement'], context=requestData)

        else:
            requestData = request.POST.dict()
            print(requestData)
            return HttpResponse(requestData)


@csrf_exempt
def UIPreview(request):
    """
    Used this function to return Preview Screen
    :param request:
    :return:
    """
    print(request.POST['filename'])
    try:
        """filePath = MM_Utiliy.getTeplatePath(MM_Utiliy,request.POST['filename'])
        f = open(filePath, "r")
        data=f.read()
        f.close()
        #print(data)

        parsehtml = MM_Utiliy.parseHtml(MM_Utiliy,data,"Preview")"""
        tempName = 'MM/'+request.POST.get('filename','')+'.html'
        print(tempName)
        return render(request, tempName ,{'Hello':"How rdsfsdfsd u"})
        #return JsonResponse("<div>{% include 'MM/UIOptions.html' %}</div>",safe=False)
    except:
        logError(log=sys.exc_info())
        exc_type, exc_value, exc_traceback = sys.exc_info()
        return HttpResponse("Faild to parse the file, Please check the logs for error\n"+repr(traceback.format_exception(exc_type, exc_value,exc_traceback)))
    #return render(request, 'MM/UIPreview_MPM.html')

