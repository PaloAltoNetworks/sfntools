import time
import random
from socket import socket
from datetime import datetime, timedelta

def sendLog(host, port, msg):
    message = msg.encode('utf-8')
    sock = socket()
    sock.connect((host, port))
    sock.sendall(message)
    sock.close()


def randomLine(afile):
    line = next(afile)
    for num, aline in enumerate(afile):
        if random.randrange(num + 2): continue
        line = aline
    return line


def calcDate(direction,ndays):
    if direction == "past":
        return f"{datetime.now() - timedelta(days=ndays):%Y/%m/%d %H:%M:%S}"
    else:
        return f"{datetime.now() + timedelta(days=ndays):%Y/%m/%d %H:%M:%S}"

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)
    #print(time.strftime(format, time.localtime(ptime)))
    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%Y/%m/%d %H:%M:%S', prop).strip()


def main():
    pass

if __name__ == "__main__":
    main()