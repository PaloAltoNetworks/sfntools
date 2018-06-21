import click
import random
import time
from lib.utils import *
from DNS.dns import *

@click.group()
def cli():
    pass

@click.command()
@click.option('--config', help='Settings file')
@click.option('--host', help='Host to send generated log messages to', default='localhost')
@click.option('--port', help='Host port to connect - default is 5514', default=5514)
def dns(config,host,port):
    click.echo("In DNS")
    if config:
        click.echo(f"File is {config}")
        host="Tester"
        port=1024
    else:
        config="DNS/dns.config"
    click.echo(f"Config is {config}")        
    click.echo(f"Host is {host}")
    click.echo(f"Port is {port}")

    flag = True
    count = 0
    start = time.time()
    numEvents = 5000
    for event in range(numEvents):
        startDate = "2018/4/19 01:30:00"
        endDate = "2018/6/15 01:30:00"
        genDate = randomDate(startDate,endDate,random.random())
        srcIP = randomLine(open("lib/srcIPs.txt"))
        srcIP = srcIP.strip()
        dstIP = randomLine(open("lib/dnsServers.txt"))
        dstIP = dstIP.strip()
        threatID = randomLine(open("lib/sigs_list.txt"))
        threatID = threatID.strip()
        severity = "informational"
        msg = f'1,{genDate},015351000011583,THREAT,spyware,2049,{genDate},{srcIP},{dstIP},192.168.55.20,{dstIP},SFN-Logging,,,dns,vsys1,trust,untrust,ethernet1/2,ethernet1/1,SFN-Log-Fowarding,{genDate},18680,1,54848,53,7771,53,0x402000,udp,sinkhole,"",{threatID},any,medium,client-to-server,50115,0x2000000000000000,192.168.0.0-192.168.255.255,United States,0,,0,,,0,,,,,,,,0,12,0,0,0,,ELA-VM-50,,,,,0,,0,,N/A,dns,AppThreat-2606-3102,0x0,0,4294967295'
        #while flag == True:
        #fileNum = random.randint(1,4)
        #fileName = f"lib/log{fileNum}.csv"
        #fileName = f"lib/logtraffic.csv"
        #line = randomLine(open(f"{fileName}"))
        #print(msg)
    
        sendLog('test.sfn',5517,msg)
        count += 1
        
    print(f"Started at {start}")
    print(f"Ended at {time.time()}")
    print(f"Time to send {count} events: {str(time.time() - start)} seconds")
    flag = False
    #time.sleep(1)
                
@click.command()
def iot():
    click.echo("In IoT")

@click.command()
def url():
    click.echo("In URL")

cli.add_command(dns)
cli.add_command(iot)
cli.add_command(url)

