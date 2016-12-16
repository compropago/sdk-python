from compropago.factory.factory import Factory
from compropago.tools.request import Request


class Service:
    def __init__(self, client):
        self.client = client

    def list_providers(self, auth=False, limit=0):
        if auth:
            uri = self.client.deploy_uri+'providers'
            keys = self.client.get_full_auth()
        else:
            uri = self.client.deploy_uri+'providers/true'
            keys = None

        if limit > 0:
            uri += '?order_total='+str(limit)

        response = Request.get(url=uri, auth=keys)

        print(response)

        return Factory.get_instance_of(class_name='ListProviders', data=response)
