from MPMUtils.Logging import logError
import sys

def DickUpdate(key,originalData,updateData):
    try:
        if key in originalData:
            originalData[key].update(updateData)

        else:
            originalData[key] = updateData
        return originalData
    except:
        logError(log=sys.exc_info())
        return originalData
    