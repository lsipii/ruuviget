from tokenize import Number
from app.Settings import Settings
from ruuvitag_sensor.ruuvi import RuuviTagSensor, RunFlag

###
# @see: https://github.com/ttu/ruuvitag-sensor
###
class RuuviGet:
    def execute(self, requestData: dict) -> list:
        self.__initialize(requestData)
        self.__fetch_data()
        return self.__get_results()

    __results: list
    __max_seconds_counter: Number
    __run_flag = None
    __macs: list

    def __initialize(self, requestData: dict):
        self.__results = []
        self.__max_seconds_counter = 6
        self.__run_flag = RunFlag()
        self.__macs = self.__resolve_input_mac_addresses(requestData)

    def __resolve_input_mac_addresses(self, requestData: dict) -> list:
        if (
            isinstance(requestData, dict)
            and "mac_addresses" in requestData
            and isinstance(requestData["mac_addresses"], list)
            and len(requestData["mac_addresses"]) > 0
        ):
            return requestData["mac_addresses"]
        return Settings().get_list("MAC_ADDRESSES", str)

    def __fetch_data(self):
        RuuviTagSensor.get_datas(self.__handle_data, self.__macs, self.__run_flag)

    def __handle_data(self, found_data):
        # Set data
        self.__results.append(found_data)
        self.__max_seconds_counter = self.__max_seconds_counter - 1

        # Set stop condition
        if isinstance(self.__macs, list) and len(self.__macs) > 0:
            if len(self.__results) >= len(self.__macs):
                self.__run_flag.running = False
        if self.__max_seconds_counter < 0:
            self.__run_flag.running = False

    def __get_results(self):
        return self.__results.copy()
