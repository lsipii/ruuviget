from time import sleep
import click

from .runner import engage
from app.utils.Settings import Settings
from app.utils.data_structures import dotdict


@click.command()
@click.argument("mac_addresses", default=None, required=False)
@click.argument("repetition_in_seconds", default=None, required=False, type=int)
def execute(mac_addresses: list = None, repetition_in_seconds: int = None):

    configuration = resolve_configuration(mac_addresses, repetition_in_seconds)
    if configuration.repetition > 0:
        while True:
            engage(configuration)
            sleep(configuration.repetition)
    else:
        engage(configuration)


def resolve_configuration(mac_addresses: list = None, repetition_in_seconds: int = None):

    # Runtime loop repetition
    repetition = 0
    if repetition_in_seconds is not None:
        if not isinstance(repetition_in_seconds, int):
            raise Exception("Bad argument type: repetition_in_seconds")
        repetition = repetition_in_seconds
    else:
        repetition = Settings().get_int("RUUVI_CLI_REPETITION_IN_SECONDS", default_value=0)

    # Resolve mac settings
    macs = None
    if mac_addresses is not None:
        macs = mac_addresses
    else:
        macs = Settings().get_list("RUUVI_MAC_ADDRESSES", list_item_type=str, default_value=None)

    # Resolve mac name settings
    mac_names = Settings().get_list(
        "RUUVI_MAC_NAMES", list_item_type=tuple, convert_to_item_type=True, default_value=[]
    )

    return dotdict(
        {
            "repetition": repetition,
            "mac_addresses": macs,
            "mac_names": mac_names,
        }
    )


if __name__ == "__main__":
    execute()
