'''
Log generator that takes in a number of events to generate. 

It will randomly pick a source IP from generated_ips.txt file in the lib dir.

Generates http log messages that the SFN2.x system is listening for via 
logstash.

The sendLogMsg() function will also randomly generate dates between the startDate
and endDate strings that are sent when it is called, so those can be updated
to reflect a time period you want to model.  

loggingURL will need to be changed to your logstash listener.
'''import json
import time
import random
import argparse
import requests
import ipaddress
from utilities import randomLine, randomDate

 
loggingURL = "http://192.168.86.140:9563"

def sendLogMsg(srcIP,startDate,endDate):
        # Generate random number of events to send from the srcIP
        # for event in range(random.randint(1,5)):
                # Grab a threat and generate a timestamp for the msg
        threatID = randomLine(open('small_sigs_list.txt'))
        timeStamp = randomDate(startDate,endDate,random.random())
        data = {"msg_gen_time": timeStamp,
                "threat_id": threatID.strip(),
                "rule": "ScriptGen - Endpoint DNS",
                "dst_ip": "192.168.55.2",
                "threat_category": "dns-wildfire",
                "src_ip": srcIP,
                "device_name": "PA-VM"
                }

        # sending post request and saving response as response object
        r = requests.post(url = loggingURL, json = data)
        print(f"Event: {data}")
                                
def main():
        numEvents = 300000     
        parser = argparse.ArgumentParser()
        parser.add_argument("-n","--number", dest = "numEvents", 
                        help = "Number of events to generate - default is 2,000",
                        default = 2000 )
        start = time.clock()
        for event in range(numEvents):
                srcIP = randomLine(open('lib/generated_ips.txt'))
                sendLogMsg(srcIP.strip(),"2017/11/1 01:30:00","2017/12/30 00:00:01")

        end = time.clock()

        print(f"Time to send {numEvents} events: {str(end - start)}") 


if __name__ == "__main__":
        main()

