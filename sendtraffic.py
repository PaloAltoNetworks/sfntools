from lib.utils import *

with open("lib/log.csv") as f:
    for line in f:
        sendLog('test.sfn',5514,line)
