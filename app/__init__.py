import traceback
from flask import Flask, request
from app.RuuviGet import RuuviGet
from app.responses import responses

app = Flask(__name__)

"""
The HTTP server request handlers
"""


@app.route("/<path>", methods=["GET", "POST"])
def ruuvigetController(path=None):

    if isinstance(path, str):

        requestData = {}
        try:
            requestData = request.json
        except Exception:
            pass

        try:
            if path == "ruuviget":
                result = RuuviGet().execute(requestData)
                return responses.generateFlaskResponse(app, result, 200)
        except Exception:
            traceback.print_exc()
            return responses.getErrorResponse(app)
    return responses.getBadAPIGatewayResponse(app)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
