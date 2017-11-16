from compropago.factory.models.feedetails import FeeDetails
from compropago.factory.models.orderinfo import OrderInfo
from compropago.factory.models.customer import Customer


class CpOrderInfo:
    id = None
    type = None
    object = None
    created = None
    paid = None
    amount = None
    livemode = None
    currency = None
    refunded = None
    fee = None
    fee_details = None
    order_info = None
    customer = None
    captured = None
    failure_message = None
    failure_code = None
    amount_refunded = None
    description = None
    dispute = None

    def __init__(self):
        self.fee_details = FeeDetails()
        self.order_info = OrderInfo()
        self.customer = Customer()
