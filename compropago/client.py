import compropago.config as config
from compropago.service import Service


class Client:
    def __init__(self, publickey, privatekey, live, contained=""):
        self.publickey = publickey
        self.privatekey = privatekey
        self.live = live
        self.contained = contained

        if live:
            self.deploy_uri = config.SETTINGS['api_live_uri']
        else:
            self.deploy_uri = config.SETTINGS['api_sandbox_uri']

        self.api = Service(self)

    def get_user(self):
        return self.privatekey

    def get_pass(self):
        return self.publickey

    def get_full_auth(self):
        return self.privatekey+':'+self.publickey
