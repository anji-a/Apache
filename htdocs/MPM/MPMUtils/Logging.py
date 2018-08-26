import logging
import datetime
import sys, traceback
logger=logging.getLogger(__name__)


def logError(*args,**kwargs):
    exc_type, exc_value, exc_traceback = kwargs.get('log')
    logger.error('excetion start at {time} and exception is {exception}'.format(time=datetime.datetime.now(),exception=kwargs.get('message','')))
    logger.error(repr(traceback.format_exception(exc_type, exc_value,exc_traceback)))



def logWarning(message):
    exc_type, exc_value, exc_traceback = message
    logger.warning(datetime.datetime.now())
    logger.warning("-->")
    logger.warning(repr(traceback.format_exception(exc_type, exc_value,exc_traceback)))


def logInfo(message):
    exc_type, exc_value, exc_traceback = message
    logger.info(datetime.datetime.now())
    logger.info("-->")
    logger.info(repr(traceback.format_exception(exc_type, exc_value,exc_traceback)))

def logMessage(*args,**kwargs):
    logger.error('{Logmessage} --> {time}'.format(Logmessage=kwargs.get('message', ''),time=datetime.datetime.now()))
