from tokenize import Number
from app.utils.Settings import Settings
from ruuvitag_sensor.ruuvi import RuuviTagSensor, RunFlag

dummy_data_set = [
    [
        "A1:CD:EF:GH:IJ:K1",
        {
            "data_format": 5,
            "humidity": 20.59,
            "temperature": 23.78,
            "pressure": 1004.29,
            "acceleration": 1009.1501374919393,
            "acceleration_x": 4,
            "acceleration_y": -48,
            "acceleration_z": 1008,
            "tx_power": 4,
            "battery": 3013,
            "movement_counter": 20,
            "measurement_sequence_number": 10271,
            "mac": "a1cdefghijk1",
        },
    ],
    [
        "A1:CD:EF:GH:IJ:K9",
        {
            "data_format": 5,
            "humidity": 18.33,
            "temperature": 20.95,
            "pressure": 1004.43,
            "acceleration": 988.2347899158377,
            "acceleration_x": -8,
            "acceleration_y": -20,
            "acceleration_z": 988,
            "tx_power": 4,
            "battery": 2978,
            "movement_counter": 104,
            "measurement_sequence_number": 10095,
            "mac": "a1cdefghijk9",
        },
    ],
]

###
# @see: https://github.com/ttu/ruuvitag-sensor
###
class RuuviGetator:
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
        return Settings().get_list("RUUVI_MAC_ADDRESSES", str)

    def __fetch_data(self):
        if Settings().get_boolean("RUUVI_DUMMY_DATA_MODE"):
            for dummyData in dummy_data_set:
                self.__handle_data(dummyData)
            self.__send_stop_signal()
        else:
            RuuviTagSensor.get_datas(self.__handle_data, self.__macs, self.__run_flag)

    def __handle_data(self, found_data):
        # Set data
        self.__results.append(found_data)
        self.__max_seconds_counter = self.__max_seconds_counter - 1

        # Set stop condition
        if isinstance(self.__macs, list) and len(self.__macs) > 0:
            if len(self.__results) >= len(self.__macs):
                self.__send_stop_signal()
        if self.__max_seconds_counter < 0:
            self.__send_stop_signal()

    def __send_stop_signal(self):
        self.__run_flag.running = False

    def __get_results(self):
        return self.__results.copy()
