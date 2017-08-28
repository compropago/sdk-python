import unittest
import time
import calendar
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

    def test_providers(self):
        res = False
        try:
            obj = Client(self.publickey, self.privatekey, self.mode)
            provs = obj.api.list_providers()

            res = (type(provs) is list and isinstance(provs[0], Provider))
        except Exception as e:
            print(e.args)

        self.assertTrue(res)

    def test_providers_limit(self):
        res = True
        try:
            obj = Client(self.publickey, self.privatekey, self.mode)
            provs = obj.api.list_providers(self.limit)

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
            provs = obj.api.list_providers(700, 'USD')

            for prov in provs:
                if prov.transaction_limit < self.limit:
                    res = False
                    break
        except Exception as e:
            print(e.args)

        self.assertTrue(res)

    def test_place_order(self):
        res = False
        try:
            obj = Client(self.publickey, self.privatekey, self.mode)
            order = Factory.get_instance_of('PlaceOrderInfo', self.order_info)

            response = obj.api.place_order(order)

            res = type(response) is NewOrderInfo
        except Exception as e:
            print(e.args)

        self.assertTrue(res)

    def test_place_order_expdate(self):
        res = False
        try:
            obj = Client(self.publickey, self.privatekey, self.mode)

            epoch = calendar.timegm(time.gmtime()) + (6 * 60 * 60)
            self.order_info['expiration_time'] = epoch

            order = Factory.get_instance_of('PlaceOrderInfo', self.order_info)

            response = obj.api.place_order(order)

            res = (epoch == response.expires_at)
        except Exception as e:
            print(e.args)

        self.assertTrue(res)

    def test_verify_order(self):
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

    def test_send_sms(self):
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

    def test_deactive_webhook(self):
        webhook_id = '6e2ebaa1-6286-422d-8dd1-69e0f84d3f35'
        res = False

        try:
            obj = Client(self.publickey, self.privatekey, self.mode)
            deactive = obj.api.deactive_webhook(webhook_id)

            if type(deactive) is Webhook and deactive.status == 'deactivated':
                res = True
        except Exception as e:
            print(e.args)

        self.assertTrue(res)

if __name__ == '__main__':
    unittest.main()
