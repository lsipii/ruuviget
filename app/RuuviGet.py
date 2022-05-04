from ruuvitag_sensor.ruuvi import RuuviTagSensor


class RuuviGet:
    def execute(self, requestData: dict) -> dict:
        return RuuviTagSensor.find_ruuvitags()
