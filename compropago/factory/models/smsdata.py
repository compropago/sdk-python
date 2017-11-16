from compropago.factory.models.smsobject import SmsObject


class SmsData:
    object = None

    def __init__(self):
        self.object = SmsObject()
