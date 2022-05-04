from tokenize import Number
from ruuvitag_sensor.ruuvi import RuuviTagSensor, RunFlag

###
# @see: https://github.com/ttu/ruuvitag-sensor
###
class RuuviGet:
    results: list
    counter: Number
    run_flag = None

    def execute(self, requestData: dict) -> dict:

        self.results = []
        self.counter = 10
        # RunFlag for stopping execution at desired time
        self.run_flag = RunFlag()

        # List of macs of sensors which will execute callback function
        macs = None

        # Exec
        RuuviTagSensor.get_datas(self.handle_data, macs, self.run_flag)

        return self.results

    def handle_data(self, found_data):
        self.results.append(found_data)
        self.counter = self.counter - 1
        if self.counter < 0:
            self.run_flag.running = False
