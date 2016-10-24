from Crypto import Random
from Crypto.Cipher import AES
import base64
import urllib
import urllib2
import json

BASE_URL = 'https://api.keyarmory.com/v1'
BS = 16

pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]

class KeyArmory:
    api_key = ''

    def __init__(self, options):
        self.api_key = options['api_key']

    def encrypt(self, data):
        request = urllib2.Request(BASE_URL + '/encryption/token', headers={'x-api-key': self.api_key})
        body = urllib2.urlopen(request)
        body = json.load(body)

        encrypted_data = self.ll_encrypt(data, body['payload']['key'])

        return 'ka:' + str(body['payload']['key_id']) + ':' + body['payload']['token'] + ':' + encrypted_data

    def decrypt(self, encrypted_string):
        pieces = encrypted_string.split(':')
        key_id = pieces[1]
        token = pieces[2]
        encrypted_data = pieces[3]

        params = urllib.urlencode({'key_id': key_id, 'token': token})
        request = urllib2.Request(BASE_URL + '/encryption/key?' + params, headers={'x-api-key': self.api_key})
        body = urllib2.urlopen(request)
        body = json.load(body)

        decrypted_data = self.ll_decrypt(encrypted_data, body['payload']['key'])

        return decrypted_data

    def ll_encrypt(self, data, key):
        raw = pad(data)
        iv = Random.new().read(AES.block_size)
        aes = AES.new(key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + aes.encrypt(raw))

    def ll_decrypt(self, data, key):
        data = base64.b64decode(data)
        iv = data[:16]
        aes = AES.new(key, AES.MODE_CBC, iv)
        return unpad(aes.decrypt(data[16:]))