from Crypto import Random
from Crypto.Cipher import AES
import base64


class KeyArmory:
    api_key = ''

    def __init__(self, options):
        self.api_key = options.api_key

    def encrypt(self, data):
        pass

    def decrypt(self, encrypted_string):
        pass

    def ll_encrypt(self, data, key):
        IV = Random.new().read(32)
        aes = AES.new(key, AES.MODE_CFB, IV)
        return base64.b64encode(aes.encrypt(data))

    def ll_decrypt(self, data, key):
        IV = Random.new().read(32)
        aes = AES.new(key, AES.MODE_CFB, IV)
        return aes.decrypt(base64.b64decode(data))