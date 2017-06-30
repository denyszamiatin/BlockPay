from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Random import random

KEY_LENGTH = 2048


class User:
    """
    Represent user in system
    """
    key_generator = KeyGenerator()

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.private_key, self.public_key = self.key_generator.generate_keys()

    def __repr__(self):
        return 'User(%s, %s, %s)' % (
            self.first_name, self.last_name, self.email
        )


class KeyGenerator:
    """
    Generate private and public keys for users
    """
    def __init__(self):
        self.generator = Random.new().read

    def generate_keys(self):
        key = RSA.generate(KEY_LENGTH, self.generator)
        return key.exportKey(), key.publickey().exportKey()


class CreateCoinTransaction:
    """
    Contain user key and coin value
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value