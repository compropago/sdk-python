from compropago.factory.models.smsdata import SmsData


class SmsInfo:
    type = None
    object = None
    data = None

    def __init__(self):
        self.data = SmsData()
