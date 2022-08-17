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
class RuuviBluetoothGetator:
    def execute(self, requestData: dict) -> list:
        action = requestData["action"] if "action" in requestData else "fetch_ruuvis"

        match action:
            case "fetch_ruuvis":
                return self.__fetch_ruuvis(requestData)
            case "fetch_macs":
                return self.__fetch_macs()

        raise Exception(f"Unknown action: {action}")

    __results: list
    __max_seconds_counter: int
    __run_flag = None
    __macs: list

    def __fetch_ruuvis(self, requestData: dict) -> list:
        self.__initialize(requestData)
        self.__fetch_data()
        return self.__get_results()

    def __fetch_macs(self) -> list:
        # Gets macs for 5 seconds
        macs_data = RuuviTagSensor.get_data_for_sensors(macs=None)

        macs = []
        for result in macs_data:
            macs.append(result[0])
        return macs

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
        return Settings().get_list("RUUVI_SERVER_MAC_ADDRESSES", str)

    def __fetch_data(self):
        if Settings().get_boolean("RUUVI_SERVER_DUMMY_DATA_MODE"):
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
            macs_met = []
            for mac in self.__macs:
                for result in self.__results:
                    if result[0] == mac:
                        if mac not in macs_met:
                            macs_met.append(mac)

            if len(macs_met) == len(self.__macs):
                self.__send_stop_signal()
        if self.__max_seconds_counter < 0:
            self.__send_stop_signal()

    def __send_stop_signal(self):
        self.__run_flag.running = False

    def __get_results(self):
        results = []
        macs_met = []
        for result in self.__results:
            if result[0] not in macs_met:
                macs_met.append(result[0])
                results.append(result)
        return results
