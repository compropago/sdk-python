from compropago.factory.models.orderinfo import OrderInfo
from compropago.factory.models.feedetails import FeeDetails
from compropago.factory.models.instructions import Instructions


class NewOrderInfo:
    id = None
    short_id = None
    object = None
    status = None
    created = None
    exp_date = None
    live_mode = None
    order_info = None
    fee_details = None
    instructions = None

    def __init__(self):
        self.order_info = OrderInfo()
        self.fee_details = FeeDetails()
        self.instructions = Instructions()
