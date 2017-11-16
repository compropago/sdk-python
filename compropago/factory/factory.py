from compropago.factory.serialize import Serialize
import json


class Factory:
    def __init__(self):
        pass

    @staticmethod
    def get_instance_of(class_name, data=None):
        if data and isinstance(data, str):
            data = json.loads(data)
        elif data and isinstance(data, dict):
            data = data

        if class_name is 'CpOrderInfo':
            return Serialize.cp_order_info(data)
        elif class_name is 'Customer':
            return Serialize.customer(data)
        elif class_name is 'EvalAuthInfo':
            return Serialize.eval_auth_info(data)
        elif class_name is 'FeeDetails':
            return Serialize.fee_details(data)
        elif class_name is 'InstructionDetails':
            return Serialize.instruction_details(data)
        elif class_name is 'Instructions':
            return Serialize.instructions(data)
        elif class_name is 'NewOrderInfo':
            return Serialize.new_order_info(data)
        elif class_name is 'OrderInfo':
            return Serialize.order_info(data)
        elif class_name is 'PlaceOrderInfo':
            return Serialize.place_order_info(data)
        elif class_name is 'Provider':
            return Serialize.provider(data)
        elif class_name is 'ListProviders':
            array_aux = []

            for provider in data:
                array_aux.append(Serialize.provider(provider))

            return array_aux
        elif class_name is 'SmsInfo':
            return Serialize.sms_info(data)
        elif class_name is 'SmsData':
            return Serialize.sms_data(data)
        elif class_name is 'SmsObject':
            return Serialize.sms_object(data)
        elif class_name is 'Webhook':
            return Serialize.webhook(data)
        elif class_name is 'ListWebhooks':
            array_aux = []

            for webhook in data:
                array_aux.append(Serialize.webhook(webhook))

            return array_aux
        else:
            raise Exception('Object not in factory.')
