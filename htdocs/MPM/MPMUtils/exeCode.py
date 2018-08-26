import sys

from django.core.cache import cache

from MPMUtils.Logging import logError,logMessage
from MPMUtils.getFilePath import getFilePath


def exeCode(*args,**kwargs):

    #print(kwargs)
    #print(args)
    #data=kwargs['data']
    cache.clear()
    retData = ''
    try:
        funname=kwargs.get('data').get('fun_name')
        codeObj = cache.get(funname+'_data')
        #print("In EXE code method", getFilePath(funname))

        if not codeObj:
            #print("exe code if block")

            fileLocation = getFilePath(funname)
            code_obj = compile(open(fileLocation).read(), funname, 'exec')
            cache.set_many({funname+'_data':open(fileLocation).read(),funname+'_location':fileLocation})

        else:
            code_obj = compile(codeObj, funname, 'exec')


        logMessage(message="Execution start for function-->"+funname)
        exec(code_obj, globals())
        retData = globals()[funname](kwargs.get('data'))
        logMessage(message="Execution End for function-->" + funname)
    except:
        logError(message="Unexpected error while execution file:"+funname, log=sys.exc_info())


    return retData