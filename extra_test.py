from compropago.client import Client

client = Client('pk_test_638e8b14112423a086', 'sk_test_9c95e149614142822f', False)

info = client.api.verify_order('ch_c3ceff55-fc8e-4877-a807-fea17bdbde29')

print(info)
