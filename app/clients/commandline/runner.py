import click

from app.services.Ruuvinator import Ruuvinator

@click.command()
@click.argument('mac_addresses', default=None, required=False)
def printRuuvis(mac_addresses=None):
    result = Ruuvinator().fetch(mac_addresses)
    if "items" in result and len(result["items"]) > 0:
        for item in result["items"]:
            click.echo(f'{item}')
    else:
        click.echo(f'No results')

if __name__ == '__main__':
    printRuuvis()