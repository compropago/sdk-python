from compropago.tools.http import Http
import json


class Request:
    @staticmethod
    def validate_response(res):
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
        http = Http(url)
        http.set_auth(auth)
        http.set_method('GET')
        http.set_extra_headers(headers)
        response = http.execute_request()

        Request.validate_response(response)

        return response

    @staticmethod
    def post(url, data=None, auth=None, headers=None):
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
        http = Http(url)
        http.set_method('DELETE')
        http.set_auth(auth)
        http.set_data(data)
        http.set_extra_headers(headers)
        response = http.execute_request()

        Request.validate_response(response)

        return response
