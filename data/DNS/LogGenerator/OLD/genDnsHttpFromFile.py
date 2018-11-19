'''
Log generator that takes in a csv file named events.csv and reads the rows in. 

Must have colums formatted in the following manner:
Source address,Destination address,Threat/Content Name

Generates http log messages that the SFN2.x system is listening for via 
logstash.

The sendLogMsg() function will also randomly generate dates between the startDate
and endDate strings that are sent when it is called, so those can be updated
to reflect a time period you want to model.  

loggingURL will need to be changed to your logstash listener.
'''
import csv
import json
import time
import random
import argparse
import requests
import ipaddress
from utilities import randomLine, randomDate

 
loggingURL = "http://54.173.131.120:9563"
     

def sendLogMsg(srcIP,dstIP,domainName,startDate,endDate):
        
        # Generate event to send from the srcIP
        
        devNum = random.randint(1,10)  # gen 1 of 3 numbers
        devName = f"CSV-FW-{devNum}"
        # Generate a random time stamp for the message
        timeStamp = randomDate(startDate,endDate,random.random())
        data = {"msg_gen_time": timeStamp,
                "threat_id": f"Bogus.data:{domainName}(12345678)",
                "rule": "ScriptGen - Endpoint DNS",
                "dst_ip": dstIP,
                "threat_category": "dns-wildfire",
                "src_ip": srcIP,
                "device_name": devName
                }

        # sending post request and saving response as response object
        r = requests.post(url = loggingURL, json = data)
        print(f"Event: {data}")
                                
def main():
        start = time.clock()
        
                
        with open('events.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                count = 1
                for row in reader:
                        if row['src_addr'] != "":
                                srcIP = row['src_addr']
                        if row['dst_addr'] != "":
                                dstIP = row['dst_addr']
                        if row['domain'] != "":
                                domainName = row['domain']
                                count += 1
                        sendLogMsg(srcIP.strip(),dstIP.strip(),domainName.strip(),"2018/01/01 01:30:00","2018/01/24 01:00:01")
        end = time.clock()

        print(f"Time to send {count} events: {str(end - start)}") 


if __name__ == "__main__":
        main()

