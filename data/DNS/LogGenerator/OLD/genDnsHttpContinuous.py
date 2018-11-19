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

 
loggingURL = "http://192.168.86.140:9563"
     

def sendLogMsg(srcIP,dstIP,domainName):
        
        # Generate event to send from the srcIP
        
        devNum = random.randint(1,4)  # gen 1 of 3 numbers
        devName = f"CSV-FW-{devNum}"
        # Generate a random time stamp for the message
        timeStamp = time.strftime('%Y/%m/%d %H:%M:%S')
        data = {"msg_gen_time": timeStamp,
                "threat_id": f"Bogus.data:{domainName}(12345678)",
                "rule": "ScriptGen - Endpoint DNS",
                "dst_ip": dstIP,
                "threat_category": "dns-wildfire",
                "src_ip": srcIP,
                "device_name": devName
                }

        # sending post request and saving response as response object
        #r = requests.post(url = loggingURL, json = data)
        print(f"Event: {data}")
                                
def main():
        # numEvents = 300000     
        # parser = argparse.ArgumentParser()
        # parser.add_argument("-n","--number", dest = "numEvents", 
        #                 help = "Number of events to generate - default is 2,000",
        #                 default = 2000 )
        start = time.clock()
        
                
        with open('events.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                interestingrow=[row for idx, row in enumerate(reader) if idx in (28,62)]  

                for row in interestingrow:
                        if row['Source address'] != "":
                                srcIP = row['Source address']
                        if row['Destination address'] != "":
                                dstIP = row['Destination address']
                        if row['Threat/Content Name'] != "":
                                domainName = row['Threat/Content Name']
                                count += 1
                        #sendLogMsg(srcIP.strip(),dstIP.strip(),domainName.strip(),"2018/01/09 01:30:00","2018/01/12 00:00:01")
                        print(f"{srcIP.strip()},{dstIP.strip()},{domainName.strip()}")
        end = time.clock()

        print(f"Time to send {count} events: {str(end - start)}") 


if __name__ == "__main__":
        main()

