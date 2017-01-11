import unittest
from compropago.client import Client
from compropago.tools.validations import Validations
from compropago.factory.factory import Factory
from compropago.factory.models.evalauthinfo import EvalAuthInfo
from compropago.factory.models.provider import Provider
from compropago.factory.models.neworderinfo import NewOrderInfo
from compropago.factory.models.cporderinfo import CpOrderInfo
from compropago.factory.models.smsinfo import SmsInfo
from compropago.factory.models.webhook import Webhook


class UnitTest(unittest.TestCase):
    def setUp(self):
        self.publickey = 'pk_test_638e8b14112423a086'
        self.privatekey = 'sk_test_9c95e149614142822f'
        self.mode = False
        self.phone_number = '5561463627'
        self.limit = 15000
        self.order_info = {
            'order_id': 123,
            'order_name': 'M4 python sdk',
            'order_price': 123.45,
            'customer_name': 'Eduardo',
            'customer_email': 'asd@asd.com',
            'payment_type': 'OXXO',
            'currency': 'MXN'
        }

    def test_create_client(self):
        res = False
        try:
            obj = Client(self.publickey, self.privatekey, self.mode)
            res = True
        except Exception as e:
            print(e.args)

        self.assertTrue(res)

    def test_eval_auth(self):
        res = False
        try:
            obj = Client(self.publickey, self.privatekey, self.mode)
            evl = Validations.eval_auth(obj)

            res = isinstance(evl, EvalAuthInfo)
        except Exception as e:
            print(e.args)

        self.assertTrue(res)

    def test_service_providers(self):
        res = False
        try:
            obj = Client(self.publickey, self.privatekey, self.mode)
            provs = obj.api.list_providers()

            res = (type(provs) is list and isinstance(provs[0], Provider))
        except Exception as e:
            print(e.args)

        self.assertTrue(res)

    def test_service_providers_limit(self):
        res = True
        try:
            obj = Client(self.publickey, self.privatekey, self.mode)
            provs = obj.api.list_providers(False, self.limit)

            for prov in provs:
                if prov.transaction_limit < self.limit:
                    res = False
                    break
        except Exception as e:
            print(e.args)

        self.assertTrue(res)

    def test_service_providers_auth(self):
        res = False
        try:
            obj = Client(self.publickey, self.privatekey, self.mode)
            provs = obj.api.list_providers(True)

            res = (type(provs) is list and isinstance(provs[0], Provider))
        except Exception as e:
            print(e.args)

        self.assertTrue(res)

    def test_service_providers_auth_limit(self):
        res = True
        try:
            obj = Client(self.publickey, self.privatekey, self.mode)
            provs = obj.api.list_providers(False, self.limit)

            for prov in provs:
                if prov.transaction_limit < self.limit:
                    res = False
                    break
        except Exception as e:
            print(e.args)

        self.assertTrue(res)

    def test_providers_currency(self):
        res = True
        try:
            obj = Client(self.publickey, self.privatekey, self.mode)
            provs = obj.api.list_providers(False, 700, 'USD')

            for prov in provs:
                if prov.transaction_limit < 15000:
                    res = False
                    break
        except Exception as e:
            print(e.args)

        self.assertTrue(res)

    def test_service_place_order(self):
        res = False
        try:
            obj = Client(self.publickey, self.privatekey, self.mode)
            order = Factory.get_instance_of('PlaceOrderInfo', self.order_info)

            response = obj.api.place_order(order)

            res = type(response) is NewOrderInfo
        except Exception as e:
            print(e.args)

        self.assertTrue(res)

    def test_service_verify_order(self):
        res = False
        try:
            obj = Client(self.publickey, self.privatekey, self.mode)
            order = Factory.get_instance_of('PlaceOrderInfo', self.order_info)

            new_order = obj.api.place_order(order)
            response = obj.api.verify_order(new_order.id)

            res = type(response) is CpOrderInfo
        except Exception as e:
            print(e.args)

        self.assertTrue(res)

    def test_service_send_sms(self):
        res = False
        try:
            obj = Client(self.publickey, self.privatekey, self.mode)
            order = Factory.get_instance_of('PlaceOrderInfo', self.order_info)

            new_order = obj.api.place_order(order)
            response = obj.api.send_sms_instructions(self.phone_number, new_order.id)

            res = type(response) is SmsInfo
        except Exception as e:
            print(e.args)

        self.assertTrue(res)

    def test_list_webhooks(self):
        res = False
        try:
            obj = Client(self.publickey, self.privatekey, self.mode)
            webs = obj.api.list_webhooks()

            res = type(webs) is list and isinstance(webs[0], Webhook)
        except Exception as e:
            print(e.args)

        self.assertTrue(res)

    def test_create_webhook(self):
        res = False
        try:
            obj = Client(self.publickey, self.privatekey, self.mode)
            webhook = obj.api.create_webhook('http://misitio.com/webhook/')

            res = type(webhook) is Webhook
        except Exception as e:
            print(e.args)

        self.assertTrue(res)

    def test_update_webhook(self):
        res = False
        try:
            obj = Client(self.publickey, self.privatekey, self.mode)
            webhook = obj.api.create_webhook('http://misitio.com/webhook/')

            update = obj.api.update_webhook(webhook.id, 'http://misitio.com/webhook/dos')

            res = type(update) is Webhook
        except Exception as e:
            print(e.args)

        self.assertTrue(res)

    def test_delete_webhook(self):
        res = False
        try:
            obj = Client(self.publickey, self.privatekey, self.mode)
            webhook = obj.api.create_webhook('http://misitio.com/webhook/dos')

            delete = obj.api.delete_webhook(webhook.id)

            res = type(delete) is Webhook
        except Exception as e:
            print(e.args)

        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()
