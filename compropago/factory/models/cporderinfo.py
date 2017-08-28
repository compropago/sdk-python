from compropago.factory.models.feedetails import FeeDetails
from compropago.factory.models.orderinfo import OrderInfo
from compropago.factory.models.customer import Customer


class CpOrderInfo:
    id = None
    short_id = None
    type = None
    object = None
    livemode = None
    created_at = None
    accepted_at = None
    expires_at = None
    paid = None
    amount = None
    currency = None
    refunded = None
    fee = None
    fee_details = None
    order_info = None
    customer = None
    api_version = None

    def __init__(self):
        self.fee_details = FeeDetails()
        self.order_info = OrderInfo()
        self.customer = Customer()
