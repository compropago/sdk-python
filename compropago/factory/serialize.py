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
from compropago.factory.models.smsinfo import SmsInfo
from compropago.factory.models.smsobject import SmsObject
from compropago.factory.models.smsdata import SmsData
from compropago.factory.models.webhook import Webhook


class Serialize:
    def __init__(self):
        pass

    @staticmethod
    def place_order_info(data=None):
        if not data:
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
                data['expiration_time'] if 'expiration_time' in data else None,
                data['image_url'] if 'image_url' in data else "",
                data['app_client_name'] if 'app_client_name' in data else "python-sdk",
                data['app_client_version'] if 'app_client_version' in data else config.SETTINGS['sdk_version']
            )

    @staticmethod
    def cp_order_info(data=None):
        if not data:
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

            return obj

    @staticmethod
    def customer(data=None):
        if not data:
            return Customer()
        else:
            obj = Customer()

            obj.customer_name = data['customer_name']
            obj.customer_email = data['customer_email']
            obj.customer_phone = data['customer_phone']

            return obj

    @staticmethod
    def eval_auth_info(data=None):
        if not data:
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
        if not data:
            return FeeDetails()
        else:
            obj = FeeDetails()

            obj.amount = data['amount'] if 'amount' in data else None
            obj.currency = data['currency'] if 'currency' in data else None
            obj.type = data['type'] if 'type' in data else None
            obj.description = data['description'] if 'description' in data else None
            obj.application = data['application'] if 'application' in data else None
            obj.tax_percent = data['tax_percent'] if 'tax_percent' in data else None
            obj.amount_refunded = data['amount_refunded'] if 'amount_refunded' in data else None
            obj.tax = data['tax'] if 'tax' in data else None

            return obj

    @staticmethod
    def instruction_details(data=None):
        if not data:
            return InstructionDetails()
        else:
            obj = InstructionDetails()

            obj.amount = data['amount'] if 'amount' in data else None
            obj.store = data['store'] if 'store' in data else None
            obj.payment_amount = data['payment_amount'] if 'payment_amount' in data else None
            obj.payment_store = data['payment_store'] if 'payment_store' in data else None
            obj.bank_account_holder_name = data['bank_account_holder_name'] if 'bank_account_holder_name' in data else None
            obj.bank_account_number = data['bank_accont_number'] if 'bank_accont_number' in data else None
            obj.bank_reference = data['bank_reference'] if 'bank_reference' in data else None
            obj.company_reference_name = data['company_reference_name'] if 'company_reference_name' in data else None
            obj.company_reference_number = data['company_reference_number'] if 'company_reference_number' in data else None
            obj.company_bank_number = data['company_bank_number'] if 'company_bank_number' in data else None
            obj.order_reference_number = data['order_reference_number'] if 'order_reference_number' in data else None
            obj.bank_name = data['bank_name'] if 'bank_name' in data else None

            return obj

    @staticmethod
    def instructions(data=None):
        if not data:
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
        if not data:
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

            return obj

    @staticmethod
    def order_info(data=None):
        if not data:
            return OrderInfo()
        else:
            obj = OrderInfo()

            obj.order_id = data['order_id'] if 'order_id' in data else None
            obj.order_price = data['order_price'] if 'order_price' in data else None
            obj.order_name = data['order_name'] if 'order_name' in data else None
            obj.payment_method = data['payment_method'] if 'payment_method' in data else None
            obj.store = data['store'] if 'store' in data else None
            obj.country = data['country'] if 'country' in data else None
            obj.image_url = data['image_url'] if 'image_url' in data else None
            obj.success_url = data['success_url'] if 'success_url' in data else None

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
        if not data:
            return SmsObject()
        else:
            obj = SmsObject()

            obj.id = data['id']
            obj.object = data['object']
            obj.short_id = data['short_id']

            return obj

    @staticmethod
    def sms_data(data=None):
        if not data:
            return SmsData()
        else:
            obj = SmsData()

            obj.object = Serialize.sms_object(data['object'])

            return obj

    @staticmethod
    def sms_info(data=None):
        if not data:
            return SmsInfo()
        else:
            obj = SmsInfo()

            obj.type = data['type']
            obj.object = data['object']
            obj.data = Serialize.sms_data(data['data'])

            return obj

    @staticmethod
    def webhook(data=None):
        if not data:
            return Webhook()
        else:
            obj = Webhook()

            obj.id = data['id'] if 'id' in data else None
            obj.url = data['url'] if 'url' in data else None
            obj.mode = data['mode'] if 'mode' in data else None
            obj.status = data['status'] if 'status' in data else None

            return obj
