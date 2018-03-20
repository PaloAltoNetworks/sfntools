'''
Log generator that takes in a number of events to generate. 

It will randomly pick a source IP from generated_ips.txt file in the lib dir.

Generates http log messages that the SFN2.x system is listening for via 
logstash.

The sendLogMsg() function will also randomly generate dates between the startDate
and endDate strings that are sent when it is called, so those can be updated
to reflect a time period you want to model.  

loggingURL will need to be changed to your logstash listener.
'''
import json
import time
import random
import requests
from utilities import randomLine, randomDate

 
loggingURL = "http://172.31.82.70:9563"

def sendLogMsg(srcIP,dstIP,timeStamp):


        devNum = random.randint(1,10)  # gen 1 of 10 numbers
        devName = f"CSV-FW-{devNum}"

        # Grab a threat and generate a timestamp for the msg
        threatID = randomLine(open('sigs_list.txt'))
        data = {"msg_gen_time": timeStamp,
                "threat_id": threatID.strip(),
                "rule": "ScriptGen - Endpoint DNS",
                "dst_ip": dstIP,
                "threat_category": "dns-wildfire",
                "src_ip": srcIP,
                "device_name": devName
                }

        # sending post request and saving response as response object
        r = requests.post(url = loggingURL, json = data)
        #print(f"Event: {data}")
                                
def main():
        numEvents = 300     

        while True:
            count = 0
            start = time.clock()
            numEvents = random.randint(10,50)
            sleepTime = random.randint(20,50)
            for event in range(numEvents):
                srcIP = randomLine(open('lib/generated_ips.txt'))
                dstIP = randomLine(open('lib/dst_ipv4.txt'))
                timeStamp = time.strftime('%Y/%m/%d %H:%M:%S')
                sendLogMsg(srcIP.strip(),dstIP.strip(),timeStamp)
                count += 1
            end = time.clock()
            print(f"Time to send {count} events: {str(end - start)}")
            time.sleep(sleepTime)



if __name__ == "__main__":
        main()

