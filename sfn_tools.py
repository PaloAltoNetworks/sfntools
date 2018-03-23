import click 

@click.group()
def cli():
    pass

@click.command()
@click.option('--file', help='Settings file')
@click.option('--host', help='Host to send generated log messages to')
def dns(file,host):
    click.echo("In DNS")
    click.echo(f"File is {file}")
    click.echo(f"Host is {host}")

@click.command()
def iot():
    click.echo("In IoT")

@click.command()
def url():
    click.echo("In URL")

cli.add_command(dns)
cli.add_command(iot)
cli.add_command(url)

