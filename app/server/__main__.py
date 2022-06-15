import traceback
from app.server.Flasker import Flasker
from app.services.RuuviBluetoothGetator import RuuviBluetoothGetator

app = Flasker(__name__)

"""
The HTTP server request handlers
"""
# Base fallback
@app.route("/", methods=["GET", "POST"])
def noNothingController():
    return base_controller("ruuviget")


@app.route("/<path>", methods=["GET", "POST"])
def base_controller(path=None):
    if isinstance(path, str):
        request_data = app.getRequestInput()
        try:
            if "client_version" not in request_data:
                raise Exception("Bad request")

            if path == "ruuviget":
                result = RuuviBluetoothGetator().execute(request_data)
                return app.generateResponse(result)
        except Exception:
            traceback.print_exc()
            return app.getErrorResponse()
    return app.getBadAPIGatewayResponse()


def execute():
    app.run(host="0.0.0.0")


if __name__ == "__main__":
    execute()
