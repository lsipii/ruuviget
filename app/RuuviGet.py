from ruuvitag_sensor.ruuvi import RuuviTagSensor, RunFlag

###
# @see: https://github.com/ttu/ruuvitag-sensor
###
class RuuviGet:
    def execute(self, requestData: dict) -> dict:

        results = []
        counter = 10
        # RunFlag for stopping execution at desired time
        run_flag = RunFlag()

        def handle_data(found_data):
            results.append(found_data)
            global counter
            counter = counter - 1
            if counter < 0:
                run_flag.running = False

        # List of macs of sensors which will execute callback function
        macs = None

        # Exec
        RuuviTagSensor.get_datas(handle_data, macs, run_flag)

        return results
