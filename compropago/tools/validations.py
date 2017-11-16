from compropago.tools.request import Request
from compropago.factory.factory import Factory


class Validations:
    @staticmethod
    def eval_auth(client):
        response = Request.get(
            client.deploy_uri+'users/auth',
            {'user': client.get_user(), 'pass': client.get_pass()}
        )
        info = Factory.get_instance_of('EvalAuthInfo', response)

        if info.code == 200:
            return info
        else:
            raise Exception('Error '+str(info.code)+': '+info.message)

    @staticmethod
    def validate_gateway(client):
        if not client:
            raise Exception('Client Object is not valid')

        client_mode = client.live

        auth_info = Validations.eval_auth(client)

        if auth_info.mode_key != auth_info.livemode:
            raise Exception('Keys are diferent of store mode')

        if client_mode != auth_info.livemode:
            raise Exception('Client mode is diferent of store mode')

        if client_mode != auth_info.mode_key:
            raise Exception('Client mode is diferent of keys mode')

        return True
