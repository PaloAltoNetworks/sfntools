#!/usr/bin/env python

import argparse
import logging
import logging.handlers



def sendLog(logObject):
    '''
    Send log to syslog server based on information in logObject
    @param dict logObject   Dictionary of info for sending the message
    '''
    syslogger = logging.getLogger('SyslogLogger')
    syslogger.setLevel(string2Level(logObject['level']))
    handler = logging.handlers.SysLogHandler(address=(logObject['host'], logObject['port']),
                                             facility=1)
    syslogger.addHandler(handler)
    syslogger.log(msg=logObject['message'],level=string2Level(logObject['level']))
    print(f"Host is {logObject['host']}")
    print(f"Port is {logObject['port']}")
    print(f"MSG is {logObject['message']}")

    
def string2Level(log_level):
    """ 
    Convert a commandline string to a proper log level
    @param string log_level     command line log level argument
    @return logging.LEVEL       the logging.LEVEL object to return
    """
    if log_level.upper() == "CRITICAL":
        return logging.CRITICAL
    if log_level.upper() == "ERROR":
        return logging.ERROR
    if log_level.upper() == "WARNING":
        return logging.WARNING
    if log_level.upper() == "INFO":
        return logging.INFO
    if log_level.upper() == "DEBUG":
        return logging.DEBUG
    return logging.NOTSET


if __name__ == "__main__":
    # Called from the command line, add the args to the parser
    parser = argparse.ArgumentParser(__file__,
                                 description="A syslog message generator")
    parser.add_argument("--host",default="localhost",
                        help="The syslog message recipient address")
    parser.add_argument("--port",type=int,default=5514,
                        help="The syslog message recipient port")
    parser.add_argument("--level",default="DEBUG",
                        help="The syslog message log level")
    parser.add_argument("--message",required=True,
                        help="The syslog message")

    # sendLog() requires an iterable, so we parse and convert 
    # when we send them
    sendLog(vars(parser.parse_args()))
    