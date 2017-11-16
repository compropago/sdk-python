import requests
import json
import base64


class Http:

    url = None
    data = None
    auth = None
    method = None
    extra_headers = None

    def __init__(self, url):
        self.url = url

    def set_method(self, method):
        """
        Set request method

        :param method: str
        :raise: Exception

        :author: Eduardo Aguilar <dante.aguilar41@gmail.com>
        """

        if method is 'GET' or method is 'POST' or method is 'PUT' or method is 'DELETE':
            self.method = method
        else:
            raise Exception('Not supported method.')

    def set_auth(self, auth):
        """
        Set request basic auth

        :param auth: list

        :author: Eduardo Aguilar <dante.aguilar41@gmail.com>
        """

        if type(auth) is dict:
            aux_auth = auth['user']+':'+auth['pass']
            self.auth = base64.b64encode(bytes(aux_auth, "utf-8")).decode("utf-8")

    def set_data(self, data):
        """
        Set data for the request

        :param data: dict

        :author: Eduardo Aguilar <dante.aguilar41@gmail.com>
        """

        if type(data) is dict and data:
            self.data = json.dumps(data)

    def set_extra_headers(self, headers):
        """
        Set request headers

        :param headers: dict

        :author: Eduardo Aguilar <dante.aguilar41@gmail.com>
        """

        if type(headers) is dict and headers:
            self.extra_headers = headers

    def execute_request(self):
        """
        Execute request with previous config

        :return: str

        :author: Eduardo Aguilar <dante.aguilar41@gmail.com>
        """

        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }

        final_headers = dict()

        if self.auth:
            headers['authorization'] = self.auth

        if self.extra_headers:
            for value in zip(headers, self.extra_headers):
                final_headers[value[0]] = value[1]
        else:
            final_headers = headers

        response = requests.request(self.method, self.url, data=self.data, headers=final_headers)
        response = json.dumps(response.json())

        return response

