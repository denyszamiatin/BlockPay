from Crypto import Random
from Crypto.PublicKey import RSA

from signature import create_signature

KEY_LENGTH = 2048


class KeyGenerator:
    """
    Generate private and public keys for users
    """
    def __init__(self):
        self.generator = Random.new().read

    def generate_keys(self):
        key = RSA.generate(KEY_LENGTH, self.generator)
        return key.exportKey(), key.publickey().exportKey()


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


class CoinTransactionDescriptor:
    """
    Contain user key and coin value
    """
    def __init__(self, public_key, private_key, value):
        self._value = value
        self._public_key = public_key

        self.hsh, self.signature = \
            create_signature(self._public_key, self._value, what_signer=private_key)

    @property
    def value(self):
        return self._value

    @property
    def public_key(self):
        return self._public_key


class TransactionPayment:
    """
    Represent transaction payment
    """
    def __init__(self, coin, receiver_public_key, sender_private_key):
        self._coin = coin
        self._receiver_public_key = receiver_public_key

        self.hsh, self.signature = \
            create_signature(self.receiver_public_key, what_signer=sender_private_key)

    @property
    def coin(self):
        return self._coin

    @property
    def receiver_public_key(self):
        return self._receiver_public_key
