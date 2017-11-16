from compropago.factory.factory import Factory
from compropago.factory.models.placeorderinfo import PlaceOrderInfo
from compropago.tools.request import Request


class Service:
    def __init__(self, client):
        self.client = client

    def list_providers(self, limit=0, currency='MXN'):
        """
        List providers depending of the transacction limit

        :param limit: int
        :param currency: str
        :return: dict

        :author: Eduardo Aguilar <dante.aguilar41@gmail.com>
        """

        uri = self.client.deploy_uri+'providers/'
        keys = {'user': self.client.get_user(), 'pass': self.client.get_pass()}
        

        if limit > 0:
            uri += '?order_total='+str(limit)

        if limit > 0 and currency and currency != 'MXN':
            uri += '&currency='+currency

        response = Request.get(url=uri, auth=keys)

        return Factory.get_instance_of(class_name='ListProviders', data=response)

    def verify_order(self, order_id):
        """
        Obtain the current status of an order

        :param order_id: str
        :return: CpOrderInfo

        :author: Eduardo Aguilar <dante.aguilar41@gmail.com>
        """

        response = Request.get(
            self.client.deploy_uri+'charges/'+order_id+'/',
            {'user': self.client.get_user(), 'pass': self.client.get_pass()}
        )

        obj = Factory.get_instance_of('CpOrderInfo', response)

        return obj

    def place_order(self, order):
        """
        Create an order

        :param order: PlaceOrderInfo
        :return: NewOrderInfo
        :raise: Exception

        :author: Eduardo Aguilar <dante.aguilar41>
        """

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

        response = Request.post(
            self.client.deploy_uri+'charges/',
            params,
            {'user': self.client.get_user(), 'pass': self.client.get_pass()}
        )

        obj = Factory.get_instance_of('NewOrderInfo', response)

        return obj

    def send_sms_instructions(self, number, order_id):
        """
        Send SMS instructions for an order

        :param number: str
        :param order_id: str
        :return: SmsInfo

        :author: Eduardo Aguilar <dante.aguilar41@gmail.com>
        """

        params = {"customer_phone": number}

        res = Request.post(
            self.client.deploy_uri+'charges/'+order_id+'/sms/',
            params,
            {'user': self.client.get_user(), 'pass': self.client.get_pass()}
        )

        obj = Factory.get_instance_of('SmsInfo', res)

        return obj

    def create_webhook(self, url):
        """
        Create a webhook

        :param url: str
        :return: Webhook

        :author: Eduardo Aguilar <dante.aguilar41@gmail.com>
        """

        params = {"url": url}

        res = Request.post(
            self.client.deploy_uri+'webhooks/stores/',
            params,
            {'user': self.client.get_user(), 'pass': self.client.get_pass()}
        )

        obj = Factory.get_instance_of('Webhook', res)

        return obj

    def update_webhook(self, webhook_id, url):
        """
        Update the URL of a webhook

        :param webhook_id: str
        :param url: str
        :return: Webhook

        :author: Eduardo Aguilar <dante.aguilar41@gmail.com>
        """

        params = {"url": url}

        res = Request.put(
            self.client.deploy_uri+'webhooks/stores/'+webhook_id+'/',
            params,
            {'user': self.client.get_user(), 'pass': self.client.get_pass()}
        )

        obj = Factory.get_instance_of('Webhook', res)

        return obj

    def delete_webhook(self, webhook_id):
        """
        Delete a webhook

        :param webhook_id: str
        :return: Webhook

        :author: Eduardo Aguilar <dante.aguilar41@gmail.com>
        """
        res = Request.delete(
            self.client.deploy_uri+'webhooks/stores/'+webhook_id+'/',
            None,
            {'user': self.client.get_user(), 'pass': self.client.get_pass()}
        )

        obj = Factory.get_instance_of('Webhook', res)

        return obj

    def list_webhooks(self):
        """
        Obtain the list of current webhooks

        :return: dict

        :author: Eduardo Aguilar <dante.aguilar41@gmail.com>
        """

        res = Request.get(
            self.client.deploy_uri+'webhooks/stores/',
            {'user': self.client.get_user(), 'pass': self.client.get_pass()}
        )

        obj = Factory.get_instance_of('ListWebhooks', res)

        return obj
