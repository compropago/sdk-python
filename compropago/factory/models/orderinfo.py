from compropago.factory.models.exchange import Exchange


class OrderInfo:
    order_id = None
    order_price = None
    order_name = None
    payment_method = None
    store = None
    country = None
    image_url = None
    success_url = None
    failed_url = None
    exchange = None

    def __init__(self):
        self.exchange = Exchange()
