from app.utils.data_structures import singleton
from lolcatfigletgnuplotprint import get_datetime_now


@singleton
class RuuviDataStore:
    def __init__(self, configuration) -> None:
        self.___mac_names = configuration.mac_names
        self.___value_groups = {}
        self.___max_value_pool_size = 3600

    def push(self, ruuvi_tags):
        timestampNow = int(get_datetime_now().timestamp())
        for ruuvi_tag in ruuvi_tags:
            name = next((name_tuple for name_tuple in self.___mac_names if name_tuple[0] == ruuvi_tag["mac"]), None)
            ruuvi_tag["name"] = name[1] if name is not None else None
            ruuvi_tag["identity"] = ruuvi_tag["name"] if ruuvi_tag["name"] is not None else ruuvi_tag["mac"]
            ruuvi_tag["timestamp"] = timestampNow

            if ruuvi_tag["identity"] not in self.___value_groups:
                self.___value_groups[ruuvi_tag["identity"]] = []

            self.___value_groups[ruuvi_tag["identity"]].append(ruuvi_tag)

            # Keep value pool size at limits
            if len(self.___value_groups[ruuvi_tag["identity"]]) > self.___max_value_pool_size:
                self.___value_groups[ruuvi_tag["identity"]] = self.___value_groups[ruuvi_tag["identity"]][
                    -self.___max_value_pool_size :
                ]

    def get(self):
        return self.___value_groups
