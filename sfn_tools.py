import click

@click.group()
def cli():
    pass

@click.command()
@click.option('--file', help='Settings file')
@click.option('--host', help='Host to send generated log messages to', default='localhost')
@click.option('--port', help='Host port to connect - default is 5514', default=5514)
def dns(file,host,port):
    click.echo("In DNS")
    if file:
        click.echo(f"File is {file}")
        host="Tester"
        port=1024        
    click.echo(f"Host is {host}")
    click.echo(f"Port is {port}")

@click.command()
def iot():
    click.echo("In IoT")

@click.command()
def url():
    click.echo("In URL")

cli.add_command(dns)
cli.add_command(iot)
cli.add_command(url)

