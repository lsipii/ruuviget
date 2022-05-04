import traceback
from app.Flasker import Flasker
from app.RuuviGet import RuuviGet

app = Flasker(__name__)

"""
The HTTP server request handlers
"""


@app.route("/<path>", methods=["GET", "POST"])
def base_controller(path=None):

    if isinstance(path, str):
        request_data = app.getRequestInput()
        try:
            if path == "ruuviget":
                result = RuuviGet().execute(request_data)
                return app.generateResponse(result)
        except Exception:
            traceback.print_exc()
            return app.getErrorResponse()
    return app.getBadAPIGatewayResponse()


def execute():
    app.run(host="0.0.0.0")


if __name__ == "__main__":
    execute()
