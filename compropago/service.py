from compropago.factory.factory import Factory
from compropago.factory.models.placeorderinfo import PlaceOrderInfo
from compropago.tools.request import Request


class Service:
    def __init__(self, client):
        self.client = client

    def get_auth(self):
        return {
            "user": self.client.get_user(),
            "pass": self.client.get_pass()
        }

    """
    # @param  [boolean] auth
    # @param  [float]   limit
    # @param  [string]  currency
    # @return [list<Provider>]
    """
    def list_providers(self, limit=0, currency='MXN'):
        uri = self.client.deploy_uri+'providers/'

        if limit > 0:
            uri += '?order_total='+str(limit)

        if limit > 0 and currency and currency != 'MXN':
            uri += '&currency='+currency

        response = Request.get(url=uri, auth=self.get_auth())

        return Factory.get_instance_of(class_name='ListProviders', data=response)

    """
    # @param  [string] order_id
    # @return [CpOrderInfo]
    """
    def verify_order(self, order_id):
        response = Request.get(self.client.deploy_uri+'charges/'+order_id+'/', self.get_auth())
        obj = Factory.get_instance_of('CpOrderInfo', response)
        return obj

    """
    # @param  [PlaceOrderInfo] order
    # @return [NewOrderInfo]
    """
    def place_order(self, order):
        if not isinstance(order, PlaceOrderInfo):
            raise Exception('Order object is not valid.')

        params = {
            "order_id": order.order_id,
            "order_name": order.order_name,
            "order_price": order.order_price,
            "customer_name": order.customer_name,
            "customer_email": order.customer_email,
            "payment_type": order.payment_type,
            "currency": order.currency,
            "expiration_time": order.expiration_time,
            "image_url": order.image_url,
            "app_client_name": order.app_client_name,
            "app_client_version": order.app_client_version
        }

        response = Request.post(self.client.deploy_uri+'charges/', params, self.get_auth())
        obj = Factory.get_instance_of('NewOrderInfo', response)

        return obj

    """
    # @param  [string] number
    # @param  [string] order_id
    # @return [SmsInfo]
    """
    def send_sms_instructions(self, number, order_id):
        params = {"customer_phone": number}

        res = Request.post(self.client.deploy_uri+'charges/'+order_id+'/sms/', params, self.get_auth())
        obj = Factory.get_instance_of('SmsInfo', res)

        return obj

    """
    # @param  [string] url
    # @return [Webhook]
    """
    def create_webhook(self, url):
        params = {"url": url}

        res = Request.post(self.client.deploy_uri+'webhooks/stores/', params, self.get_auth())
        obj = Factory.get_instance_of('Webhook', res)

        return obj

    """
    # @param  [string] webhook_id
    # @param  [string] url
    # @return [Webhook]
    """
    def update_webhook(self, webhook_id, url):
        params = {"url": url}

        res = Request.put(self.client.deploy_uri+'webhooks/stores/'+webhook_id+'/', params, self.get_auth())
        obj = Factory.get_instance_of('Webhook', res)

        return obj

    """
    # @param  [string] webhook_id
    # @return [Webhook]
    """
    def delete_webhook(self, webhook_id):
        res = Request.delete(self.client.deploy_uri+'webhooks/stores/'+webhook_id+'/', None, self.get_auth())
        obj = Factory.get_instance_of('Webhook', res)

        return obj

    """
    # @return [list<Webhook>]
    """
    def list_webhooks(self):
        res = Request.get(self.client.deploy_uri+'webhooks/stores/', self.get_auth())
        obj = Factory.get_instance_of('ListWebhooks', res)

        return obj
