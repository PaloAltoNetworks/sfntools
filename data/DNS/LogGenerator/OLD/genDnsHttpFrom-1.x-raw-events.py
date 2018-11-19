'''
Log generator that takes in a csv file named rawevents.csv and reads the rows in. 

This is to port over SFN1.x to 2.x 

Must have colums formatted in the following manner, but these can be in any 
order within the csv file - the headings just have to be named correctly:
Source address,Destination address,Threat/Content Name,Generate Time,device_nam

* - yes it is device_nam, that is the way the raw events were in the raw log
csv files used for testing, so it probably is that way.  

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

 
loggingURL = "http://192.168.86.140:9563"
     

def sendLogMsg(srcIP,dstIP,domainName,timeStamp,devName):
        
        # Generate event to send from the srcIP
        
        data = {"msg_gen_time": timeStamp,
                "threat_id": domainName,
                "rule": "Endpoint DNS",
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
        
                
        with open('uscellevents.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                count = 1
                for row in reader:
                        if row['Source address'] != "":
                            srcIP = row['Source address']
                        if row['Destination address'] != "":
                            dstIP = row['Destination address']
                        if row['Threat/Content Name'] != "":
                            domainName = row['Threat/Content Name']
                        if row['Generate Time'] != "":
                            genTime = row['Generate Time']
                        if row['device_nam'] != "":
                            deviceName = row['device_nam']
                            count += 1
                        sendLogMsg(srcIP.strip(),dstIP.strip(),domainName.strip(),
                                    genTime.strip(),deviceName.strip())
        end = time.clock()

        print(f"Time to send {count} events: {str(end - start)}") 


if __name__ == "__main__":
        main()

