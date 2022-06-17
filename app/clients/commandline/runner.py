from app.services.RuuviRequester import RuuviRequester
from lolcatfigletgnuplotprint import lolcat_figlet_print, plot_print, clear_screen
from lolcatfigletgnuplotprint.utils.runtime import check_shell_apps_installed
from app.utils.RuuviDataStore import RuuviDataStore
from app.utils.Settings import Settings
from .__init__ import __VERSION_NAME__

HAS_GNUPLOT_INSTALLED = "gnuplot" in check_shell_apps_installed(["gnuplot"])


def engage(configuration, initial_run: bool = False):

    description_rows = []
    plot_value_groups = []

    try:

        if initial_run:
            clear_screen("Loading..")

        # Fetch
        ruuvi_data_groups = ___fetch_ruuvi_data(configuration)

        for indetifier in ruuvi_data_groups:
            ruuvi_tags = ruuvi_data_groups[indetifier]

            plot_value_groups.append(
                {
                    "title": indetifier,
                    "values": list(
                        map(
                            lambda rv: {"value": rv["data"]["temperature"], "timestamp": rv["timestamp"]},
                            ruuvi_tags,
                        )
                    ),
                }
            )

            if len(ruuvi_tags) > 0:
                latest_ruuvi_tag = ruuvi_tags[-1]
                row_values = ___gather_row_values(latest_ruuvi_tag)
                description_rows.append(" - ".join(row_values))
            else:
                description_rows.append(f"{indetifier}: no new results")
    except Exception as e:
        description_rows.append(f"Failure: {e}")
        raise e

    # Draw
    if not HAS_GNUPLOT_INSTALLED or Settings().get_boolean("RUUVI_CLI_SIMPLE_OUTPUT"):
        lolcat_figlet_print(description_text="\n".join(description_rows), print_vertical_margins=False)
    else:
        plot = plot_print(value_groups=plot_value_groups, output_only_as_return_value=True)
        lolcat_figlet_print(message=plot, description_text="\n".join(description_rows), heading_text="Temperature")


def ___fetch_ruuvi_data(configuration):
    ruuvi_tags = RuuviRequester().fetch(client_version=__VERSION_NAME__, mac_addresses=configuration.mac_addresses)
    RuuviDataStore(configuration).push(ruuvi_tags)
    return RuuviDataStore().get()


def ___gather_row_values(ruuvi_tag) -> list:
    row_values = []

    row_values.append(f'Mac: {ruuvi_tag["mac"]}')
    if ruuvi_tag["name"] is not None:
        row_values.append(f'Name: {ruuvi_tag["name"]}')
    row_values.append(f'Temperature: {ruuvi_tag["data"]["temperature"]}')
    row_values.append(f'Humidity: {ruuvi_tag["data"]["humidity"]}')

    return row_values
