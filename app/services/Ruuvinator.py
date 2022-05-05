from app.services.Requester import Requester
from app.utils.Settings import Settings

class Ruuvinator():
    def fetch(self, mac_addresses: list = []) -> list:
        ruuvi_getator_endpoint_url = Settings().get_setting("RUUVI_GETATOR_SERVICE_URL", "http://localhost:5000/ruuviget")
        response = Requester().post(url=ruuvi_getator_endpoint_url, data={"mac_addresses": mac_addresses})

        if "items" in response and len(response["items"]) > 0:
            return list(map(lambda item: {"mac": item[0], "data": item[1]}, response["items"]))
        return []