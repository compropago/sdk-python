from compropago.tools.http import Http
import json


class Request:
    @staticmethod
    def validate_response(res):
        """
        Validate if the request return some error

        :param res: str
        :return: bool
        :raise: Exception

        :author: Eduardo Aguilar <dante.aguilar41@gmail.com>
        """

        if res:
            aux = json.loads(res)

            if 'type' in aux and aux['type'] == 'error':
                raise Exception('Error : '+aux['message'])
            else:
                return True
        else:
            raise Exception('Empty response.')

    @staticmethod
    def get(url, auth=None, headers=None):
        """
        Excute GET request

        :param url: str
        :param auth: dict
        :param headers: dict
        :return: str

        :author: Eduardo Aguilar <dante.aguilar41@gmail.com>
        """

        http = Http(url)
        http.set_auth(auth)
        http.set_method('GET')
        http.set_extra_headers(headers)
        response = http.execute_request()

        Request.validate_response(response)

        return response

    @staticmethod
    def post(url, data=None, auth=None, headers=None):
        """
        Excute POST request

        :param url: str
        :param data: dict
        :param auth: dict
        :param headers: dict
        :return: str

        :author: Eduardo Aguilar <dante.aguilar41@gmail.com>
        """

        http = Http(url)
        http.set_method('POST')
        http.set_auth(auth)
        http.set_data(data)
        http.set_extra_headers(headers)
        response = http.execute_request()

        Request.validate_response(response)

        return response

    @staticmethod
    def put(url, data=None, auth=None, headers=None):
        """
        Excute PUT request

        :param url: str
        :param data: dict
        :param auth: dict
        :param headers: dict
        :return: str

        :author: Eduardo Aguilar <dante.aguilar41@gmail.com>
        """

        http = Http(url)
        http.set_method('PUT')
        http.set_auth(auth)
        http.set_data(data),
        http.set_extra_headers(headers)
        response = http.execute_request()

        Request.validate_response(response)

        return response

    @staticmethod
    def delete(url, data=None, auth=None, headers=None):
        """
        Excute DELETE request

        :param url: str
        :param data: dict
        :param auth: dict
        :param headers: dict
        :return: str

        :author: Eduardo Aguilar <dante.aguilar41@gmail.com>
        """

        http = Http(url)
        http.set_method('DELETE')
        http.set_auth(auth)
        http.set_data(data)
        http.set_extra_headers(headers)
        response = http.execute_request()

        Request.validate_response(response)

        return response
