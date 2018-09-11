import time
import click
import random

from datetime import datetime, timedelta

from lib.utils import *
from DNS.dns import *

@click.group()
def cli():
    pass

@click.command()
@click.option('--config', help='Settings file', default='~/.panrc')
@click.option('--host', help='Host to send generated log messages to', default='localhost')
@click.option('--port', help='Host port to connect - default is 5514', default=5514)
@click.option('--days_past', help='Number of days in past to generate events', default=9)
@click.option('--days_future', help='Number of days in the future to generate events', default=100)
@click.option('--tne',  help='Total number of events to generate', default=1000000)
@click.option('--pack', help='Content pack name', default='AppThreat-scriptGen')


def dns(config,host,port,tne,days_past,days_future,pack):
    if config:
        click.echo(f"File is {config}")
    
    click.echo("In DNS")  
    click.echo(f"Host is {host}")
    click.echo(f"Port is {port}")

    count = 0
    start = time.time()

    # Do this until we reach the max number of events to send
    while count < tne:
        # Generate a random number of events to send and sleep between each send
        numEvents = random.randint(1,25)
        sleepTime = random.randint(1,3)
        for event in range(numEvents):
            startDate = calcDate("past",days_past)
            endDate = calcDate("future",days_future)
            # Generate a random date that is in the date range we want
            genDate = randomDate(startDate,endDate,random.random())
            # Get the month so we know which customer file to use
            tempDate = datetime.strptime(genDate, "%Y/%m/%d %H:%M:%S")
            csvFile = f"data/customerWireless{tempDate.month:02d}.csv"
            srcLine = randomLine(open(csvFile)).rstrip("\n").split(",")
            srcIP = srcLine[-1]
            IMSI = srcLine[-2]
            IMEI = srcLine[-3]
            dstIP = randomLine(open("data/dnsServers.txt"))
            dstIP = dstIP.strip()
            threatID = randomLine(open("data/sigsList.txt"))
            threatID = threatID.strip()
            severity = "medium"
            msg = f'1,{genDate},015351000011583,THREAT,dns,2049,{genDate},{srcIP},{dstIP},192.168.55.20,{dstIP},SFN-Logging,,,dns,vsys1,trust,untrust,ethernet1/2,ethernet1/1,SFN-Log-Fowarding,{genDate},18680,1,54848,53,7771,53,0x402000,udp,sinkhole,"",{threatID},any,medium,client-to-server,50115,0x2000000000000000,192.168.0.0-192.168.255.255,United States,0,,0,,,0,,,,,,,,0,12,0,0,0,,FW-{sleepTime},,,,,{IMSI},{IMEI},0,,N/A,dns,{pack},0x0,0,4294967295'
            # We now have the log message built - send it.
            sendLog(f"{host}",port,msg)
            

        count += numEvents

        # Keep the following to use for troubleshooting performance issues later    
        # print(f"Started at {start}")
        # print(f"Ended at {time.time()}")
        # print(f"Time to send {count} events: {str(time.time() - start)} seconds")
                       
@click.command()
def iot():
    click.echo("In IoT")

@click.command()
def url():
    click.echo("In URL")

@click.command()
@click.option('--config', help='Settings file', default='~/.panrc')
@click.option('--host', help='Host to send generated log messages to', default='localhost')
@click.option('--port', help='Host port to connect - default is 5514', default=5514)
@click.option('--log', help='Log to replay into SFN', default='lib/logtraffic.csv')
def replay(config,log,host,port):
    '''
    Quick option to replay a log download from an pan-os based system.  Using 
    defaults it will replay the log, line by line, to localhost @ port 5514 
    which logstash should be listening to. 

    :returns: nothing
    '''
    if config:
        click.echo(f"File is {config}")

    with open(log) as f:
        for line in f:
            sendLog(host,port,line.rstrip())
            time.sleep(1)

cli.add_command(dns)
cli.add_command(iot)
cli.add_command(url)
cli.add_command(replay)

