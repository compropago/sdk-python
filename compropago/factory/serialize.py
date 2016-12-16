import compropago.config as config
from compropago.factory.models.placeorderinfo import PlaceOrderInfo
from compropago.factory.models.cporderinfo import CpOrderInfo
from compropago.factory.models.customer import Customer
from compropago.factory.models.evalauthinfo import EvalAuthInfo
from compropago.factory.models.feedetails import FeeDetails
from compropago.factory.models.instructiondetails import InstructionDetails
from compropago.factory.models.instructions import Instructions
from compropago.factory.models.neworderinfo import NewOrderInfo
from compropago.factory.models.orderinfo import OrderInfo
from compropago.factory.models.provider import Provider
from compropago.factory.models.smsobject import SmsObject
from compropago.factory.models.smsdata import SmsData
from compropago.factory.models.webhook import Webhook


class Serialize:
    def __init__(self):
        pass

    @staticmethod
    def place_order_info(data=None):
        if data is None:
            return PlaceOrderInfo(None, None, None, None, None)
        else:
            return PlaceOrderInfo(
                data['order_id'],
                data['order_name'],
                data['order_price'],
                data['customer_name'],
                data['customer_email'],
                data['payment_type'] if 'payment_type' in data else 'OXXO',
                data['currency'] if 'currency' in data else 'MXN',
                data['image_url'] if 'image_url' in data else "",
                data['app_client_name'] if 'app_client_name' in data else "python-sdk",
                data['app_client_version'] if 'app_client_version' in data else config.SETTINGS['sdk_version']
            )

    @staticmethod
    def cp_order_info(data=None):
        if data is None:
            return CpOrderInfo()
        else:
            obj = CpOrderInfo()

            obj.id = data['id']
            obj.type = data['type']
            obj.object = data['object']
            obj.created = data['created']
            obj.paid = data['paid']
            obj.amount = data['amount']
            obj.livemode = data['livemode']
            obj.currency = data['currency']
            obj.refunded = data['refunded']
            obj.fee = data['fee']

            obj.fee_details = Serialize.fee_details(data['fee_details'])
            obj.order_info = Serialize.order_info(data['order_info'])
            obj.customer.customer_name = Serialize.customer(data['customer'])

            obj.captured = data['captured']
            obj.failure_message = data['failure_message']
            obj.failure_code = data['failure_code']
            obj.amount_refunded = data['amount_refunded']
            obj.description = data['description']
            obj.dispute = data['dispute']

    @staticmethod
    def customer(data=None):
        if data is None:
            return Customer()
        else:
            obj = Customer()

            obj.customer_name = data['customer_name']
            obj.customer_email = data['customer_email']
            obj.customer_phone = data['customer_phone']

            return obj

    @staticmethod
    def eval_auth_info(data=None):
        if data is None:
            return EvalAuthInfo()
        else:
            obj = EvalAuthInfo()

            obj.type = data['type']
            obj.livemode = data['livemode']
            obj.mode_key = data['mode_key']
            obj.message = data['message']
            obj.code = data['code']

            return obj

    @staticmethod
    def fee_details(data=None):
        if data is None:
            return FeeDetails()
        else:
            obj = FeeDetails()

            obj.amount = data['amount']
            obj.currency = data['currency']
            obj.type = data['type']
            obj.description = data['description']
            obj.application = data['application']
            obj.amount_refunded = data['amount_refunded']
            obj.tax = data['tax']

            return obj

    @staticmethod
    def instruction_details(data=None):
        if data is None:
            return InstructionDetails()
        else:
            obj = InstructionDetails()

            obj.amount = data['amount']
            obj.store = data['store']
            obj.payment_amount = data['payment_amount']
            obj.payment_store = data['payment_store']
            obj.bank_account_holder_name = data['bank_account_holder_name']
            obj.bank_account_number = data['banl_accont_number']
            obj.bank_reference = data['bank_reference']
            obj.company_reference_name = data['company_reference_name']
            obj.company_reference_number = data['company_reference_number']
            obj.company_bank_number = data['company_bank_number']
            obj.order_reference_number = data['order_reference_number']
            obj.bank_name = data['bank_name']

            return obj

    @staticmethod
    def instructions(data=None):
        if data is None:
            return Instructions()
        else:
            obj = Instructions()

            obj.description = data['description']
            obj.step_1 = data['step_1']
            obj.step_2 = data['step_2']
            obj.step_3 = data['step_3']
            obj.note_extra_comition = data['note_extra_comition']
            obj.note_expiration_date = data['note_expiration_date']
            obj.note_confirmation = data['note_confirmation']

            obj.details = Serialize.instruction_details(data['details'])

            return obj

    @staticmethod
    def new_order_info(data=None):
        if data is None:
            return NewOrderInfo()
        else:
            obj = NewOrderInfo()

            obj.id = data['id']
            obj.short_id = data['short_id']
            obj.object = data['object']
            obj.status = data['status']
            obj.created = data['created']
            obj.exp_date = data['exp_date']
            obj.live_mode = data['live_mode']
            obj.order_info = Serialize.order_info(data['order_info'])
            obj.fee_details = Serialize.fee_details(data['fee_details'])
            obj.instructions = Serialize.instructions(data['instructions'])

    @staticmethod
    def order_info(data=None):
        if data is None:
            return OrderInfo()
        else:
            obj = OrderInfo()

            obj.order_id = data['order_id']
            obj.order_price = data['order_price']
            obj.order_name = data['order_name']
            obj.payment_method = data['payment_method']
            obj.store = data['store']
            obj.country = data['country']
            obj.image_url = data['image_url']
            obj.success_url = data['success_url']

            return obj

    @staticmethod
    def provider(data=None):
        if not data:
            return Provider()
        else:
            obj = Provider()

            obj.name = data['name']
            obj.store_image = data['store_image']
            obj.is_active = data['is_active']
            obj.internal_name = data['internal_name']
            obj.image_small = data['image_small']
            obj.image_medium = data['image_medium']
            obj.image_large = data['image_large']
            obj.transaction_limit = data['transaction_limit']
            obj.rank = data['rank']

            return obj

    @staticmethod
    def sms_object(data=None):
        if data is None:
            return SmsObject()
        else:
            obj = SmsObject()

            obj.id = data['id']
            obj.object = data['object']
            obj.short_id = data['short_id']

            return obj

    @staticmethod
    def sms_data(data=None):
        if data is None:
            return SmsData()
        else:
            obj = SmsData()

            obj.object = Serialize.sms_object(data['object'])

            return obj

    @staticmethod
    def webhook(data=None):
        if data is None:
            return Webhook()
        else:
            obj = Webhook()

            obj.id = data['id']
            obj.url = data['url']
            obj.mode = data['mode']
            obj.status = data['status']

            return obj
