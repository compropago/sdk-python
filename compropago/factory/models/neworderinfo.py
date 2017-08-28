from compropago.factory.models.orderinfo import OrderInfo
from compropago.factory.models.feedetails import FeeDetails
from compropago.factory.models.instructions import Instructions
from compropago.factory.models.customer import Customer


class NewOrderInfo:
    id = None
    short_id = None
    type = None
    object = None
    created_at = None
    accepted_at = None
    expires_at = None
    paid = None
    amount = None
    livemode = None
    currency = None
    refunded = None
    fee = None
    fee_details = None
    order_info = None
    customer = None
    instructions = None
    api_version = None

    def __init__(self):
        self.order_info = OrderInfo()
        self.fee_details = FeeDetails()
        self.instructions = Instructions()
        self.customer = Customer()
