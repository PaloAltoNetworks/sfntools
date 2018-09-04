from lib.utils import *

with open("lib/logtraffic.csv") as f:
    for line in f:
        sendLog('23.100.59.161',5514,line)
