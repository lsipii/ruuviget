import json

###
# Flask responses
###

"""
Generates a flask response
"""


def generateFlaskResponse(app, response: dict, statusCode: int = 200):
    responseBody = json.dumps(response)
    return app.response_class(
        response=responseBody,
        status=statusCode,
        mimetype="application/json",
    )


"""
Returns a bad API gateway response
"""


def getBadAPIGatewayResponse(app):
    return generateFlaskResponse(app, {"message": "Invalid API endpoint"}, 404)


"""
Returns a good API gateway response
"""


def getGoodAPIGatewayResponse(app):
    return generateFlaskResponse(app, {"message": "OK"}, 200)


"""
Returns a bad API gateway response
"""


def getBadRequestResponse(app):
    return generateFlaskResponse(app, {"message": "Bad Request"}, 400)


"""
Returns an access denied response
"""


def getAccessDeniedReponse(app):
    return generateFlaskResponse(app, {"message": "Access denied"}, 401)


"""
Returns a bad API gateway response
"""


def getErrorResponse(app, errorMessage: str = "An error occurred"):
    return generateFlaskResponse(app, {"message": errorMessage}, 500)
