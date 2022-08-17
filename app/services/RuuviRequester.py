from app.services.Requester import Requester
from app.utils.Settings import Settings


class RuuviRequester:
    def fetch(self, client_version: str, mac_addresses: list = [], action: str = "fetch_ruuvis") -> list:
        ruuvi_getator_endpoint_url = Settings().get_setting("RUUVI_CLI_SERVICE_URL", "http://localhost:5000/ruuviget")
        response = Requester().post(
            url=ruuvi_getator_endpoint_url,
            data={"client_version": client_version, "mac_addresses": mac_addresses, "action": action},
        )

        if response["statusCode"] != 200:
            raise Exception(f"Bad response: {response['reason']}")

        if "items" in response and len(response["items"]) > 0:
            return list(map(lambda item: {"mac": item[0], "data": item[1]}, response["items"]))
        return []
