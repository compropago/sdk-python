from compropago.factory.factory import Factory
from compropago.factory.models.placeorderinfo import PlaceOrderInfo
from compropago.tools.request import Request
from compropago.tools.validations import Validations


class Service:
    def __init__(self, client):
        self.client = client

    def list_providers(self, auth=False, limit=0):
        if auth:
            Validations.validate_gateway(self.client)

            uri = self.client.deploy_uri+'providers'
            keys = self.client.get_full_auth()
        else:
            uri = self.client.deploy_uri+'providers/true'
            keys = None

        if limit > 0:
            uri += '?order_total='+str(limit)

        response = Request.get(url=uri, auth=keys)

        return Factory.get_instance_of(class_name='ListProviders', data=response)

    def verify_order(self, order_id):
        Validations.validate_gateway(self.client)

        response = Request.get(self.client.deploy_uri+'charges/'+order_id+'/', self.client.get_full_auth())
        obj = Factory.get_instance_of('CpOrderInfo', response)

        return obj

    def place_order(self, order):
        if not isinstance(order, PlaceOrderInfo):
            raise Exception('Order object is not valid.')

        Validations.validate_gateway(self.client)

        params = {
            "order_id": order.order_id,
            "order_name": order.order_name,
            "order_price": order.order_price,
            "customer_name": order.customer_name,
            "customer_email": order.customer_email,
            "payment_type": order.payment_type,
            "currency": order.currency,
            "image_url": order.image_url,
            "app_client_name": order.app_client_name,
            "app_client_version": order.app_client_version
        }

        response = Request.post(self.client.deploy_uri+'charges/', self.client.get_full_auth(), params)

        obj = Factory.get_instance_of('NewOrderInfo', response)

        return obj

    def send_sms_instructions(self, number, order_id):
        Validations.validate_gateway(self.client)

        params = {"customer_phone": number}

        res = Request.post(self.client.deploy_uri+'charges/'+order_id+'/sms', self.client.get_full_auth(), params)

        print(res)

        obj = Factory.get_instance_of('SmsInfo', res)

        return obj

    def create_webhook(self, url):
        Validations.validate_gateway(self.client)

        params = {"url": url}

        res = Request.post(self.client.deploy_uri+'webhooks/stores/', self.client.get_full_auth(), params)

        obj = Factory.get_instance_of('Webhook', res)

        return obj

    def update_webhook(self, webhook_id, url):
        Validations.validate_gateway(self.client)

        params = {"url": url}

        res = Request.put(self.client.deploy_uri+'webhooks/stores/'+webhook_id+'/', self.client.get_full_auth(), params)

        obj = Factory.get_instance_of('Webhook', res)

        return obj

    def delete_webhook(self, webhook_id):
        Validations.validate_gateway(self.client)

        res = Request.delete(self.client.deploy_uri+'webhooks/stores/'+webhook_id+'/', self.client.get_full_auth())

        obj = Factory.get_instance_of('Webhook', res)

        return obj

    def list_webhooks(self):
        Validations.validate_gateway(self.client)

        res = Request.get(self.client.deploy_uri+'webhooks/stores/', self.client.get_full_auth())

        obj = Factory.get_instance_of('ListWebhooks', res)

        return obj
