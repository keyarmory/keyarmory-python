import unittest
import keyarmory

keyarmory = keyarmory.KeyArmory({
    'api_key': 'f0e4c2f76c58916ec258f246851bea091d14d4247a2fc3e18694461b1816e13b'
})

class TestKeyArmory(unittest.TestCase):

    def test_all(self):
        original_text = 'test'

        encrypted = keyarmory.encrypt(original_text)
        decrypted = keyarmory.decrypt(encrypted)

        self.assertEqual(original_text, decrypted)

if __name__ == '__main__':
    unittest.main()