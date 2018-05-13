import click
import random
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

    while True:
        fileNum = random.randint(1,4)
        fileName = f"lib/log{fileNum}.csv"
        line = randomLine(open(f"{fileName}"))
        sendLog('test.sfn',5514,line)
        time.sleep(1)
                
@click.command()
def iot():
    click.echo("In IoT")

@click.command()
def url():
    click.echo("In URL")

cli.add_command(dns)
cli.add_command(iot)
cli.add_command(url)

