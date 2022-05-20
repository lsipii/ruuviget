import click
from app.services.RuuviRequester import RuuviRequester


def engage(configuration):

    # Clear term
    click.clear()

    try:
        # Fetch
        ruuvi_tags = RuuviRequester().fetch(configuration.mac_addresses)

        # Draw
        if len(ruuvi_tags) > 0:
            for ruuvi_tag in ruuvi_tags:
                name = next(
                    (name_tuple for name_tuple in configuration.mac_names if name_tuple[0] == ruuvi_tag["mac"]), None
                )
                ruuvi_tag["name"] = name[1] if name is not None else None

            # Sort by mac
            sorted_ruuvi_tags = sorted(ruuvi_tags, key=lambda rt: rt["mac"])

            # Draw
            for ruuvi_tag in sorted_ruuvi_tags:
                row_values = gather_row_values(ruuvi_tag)
                click.echo(" - ".join(row_values))
        else:
            click.echo(f"No results")
    except Exception as e:
        click.echo(f"Failure: {e}")


def gather_row_values(ruuvi_tag) -> list:
    row_values = []

    row_values.append(f'Mac: {ruuvi_tag["mac"]}')
    if ruuvi_tag["name"] is not None:
        row_values.append(f'Name: {ruuvi_tag["name"]}')
    row_values.append(f'Temperature: {ruuvi_tag["data"]["temperature"]}')
    row_values.append(f'Humidity: {ruuvi_tag["data"]["humidity"]}')

    return row_values
