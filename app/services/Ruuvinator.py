from app.services.Requester import Requester
from app.utils.Settings import Settings

class Ruuvinator():
    def fetch(self, mac_addresses: list = []):
        ruuvi_getator_endpoint_url = Settings().get_setting("RUUVI_GETATOR_SERVICE_URL", "http://localhost:5000/ruuviget")
        response = Requester().post(url=ruuvi_getator_endpoint_url, data={"mac_addresses": mac_addresses})
        return response