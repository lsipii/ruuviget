from flask import Flask, request

# Hide flask default banner: https://stackoverflow.com/a/72145430
import flask.cli

flask.cli.show_server_banner = lambda *args: None

import json


class Flasker(Flask):
    def getRequestInput(self) -> dict:
        """
        Parses request input
        """
        requestData = {}
        try:
            requestData = request.json
        except Exception:
            pass
        return requestData

    ###
    # Flask responses
    ###

    def generateResponse(self, response: dict, statusCode: int = 200):
        """
        Generates a flask response
        """
        responseBody = json.dumps(response)
        return self.response_class(
            response=responseBody,
            status=statusCode,
            mimetype="application/json",
        )

    def getBadAPIGatewayResponse(self):
        """
        Returns a bad API gateway response
        """
        return self.generateResponse({"message": "Invalid API endpoint"}, 404)

    def getGoodAPIGatewayResponse(self):
        """
        Returns a good API gateway response
        """
        return self.generateResponse({"message": "OK"}, 200)

    def getBadRequestResponse(self):
        """
        Returns a bad API gateway response
        """
        return self.generateResponse({"message": "Bad Request"}, 400)

    def getAccessDeniedReponse(self):
        """
        Returns an access denied response
        """
        return self.generateResponse({"message": "Access denied"}, 401)

    def getErrorResponse(self, errorMessage: str = "An error occurred"):
        """
        Returns a bad API gateway response
        """
        return self.generateResponse({"message": errorMessage}, 500)
