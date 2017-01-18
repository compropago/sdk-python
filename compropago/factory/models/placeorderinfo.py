import compropago.config as config


class PlaceOrderInfo:
    order_id = None
    order_name = None
    order_price = None
    customer_name = None
    customer_email = None
    payment_type = None
    currency = None
    expiration_time = None
    image_url = None
    app_client_name = None
    app_client_version = None

    def __init__(
        self,
        order_id,
        order_name,
        order_price,
        customer_name,
        customer_email,
        payment_type="OXXO",
        currency="MXN",
        expiration_time=None,
        image_url="",
        app_client_name="python-sdk",
        app_client_version=config.SETTINGS['sdk_version']
    ):
        self.order_id = order_id
        self.order_name = order_name
        self.order_price = order_price
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.payment_type = payment_type
        self.currency = currency
        self.expiration_time = expiration_time
        self.image_url = image_url
        self.app_client_name = app_client_name
        self.app_client_version = app_client_version
