from requests import post, get


class Requester:
    request_timeout_secs = 30

    def get(self, url: str, data: dict = None, headers: dict = None) -> dict:
        return self.fetch("GET", url, data, headers)

    def post(self, url: str, data: dict = None, headers: dict = None) -> dict:
        return self.fetch("POST", url, data, headers)

    def fetch(self, method: str, url: str, data: dict = None, headers: dict = None) -> dict:
        """
        Sends a request
        """
        responseData = {}

        try:
            if method == "GET":
                response = get(url, params=data, headers=headers, timeout=self.request_timeout_secs)
            else:
                response = post(url, json=data, headers=headers, timeout=self.request_timeout_secs)

            if (
                "Content-Type" in response.request.headers
                and response.request.headers["Content-Type"] == "application/json"
            ):
                try:
                    parsedResponse = response.json()
                    if isinstance(parsedResponse, list):
                        responseData["items"] = parsedResponse
                    else:
                        responseData = parsedResponse

                    if "statusCode" not in responseData:
                        responseData["statusCode"] = response.status_code
                    if "reason" not in responseData:
                        responseData["reason"] = response.reason
                except Exception:
                    responseData["statusCode"] = response.status_code
                    responseData["reason"] = response.reason
                    responseData["text"] = response.text
                    pass
            else:
                responseData["statusCode"] = response.status_code
                responseData["reason"] = response.reason
                responseData["text"] = response.text
        except Exception as requestErr:
            responseData["statusCode"] = -1
            responseData["reason"] = str(requestErr)
        return responseData
