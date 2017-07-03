from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
import pickle

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


class CoinTransactionDescriptor:
    """
    Contain user key and coin value
    """
    def __init__(self, public_key, private_key, value):
        self._value = value
        self._public_key = public_key
        self.hsh = SHA.new(pickle.dumps((self._public_key, self._value)))
        signer = PKCS1_v1_5.new(RSA.importKey(private_key))
        self.signature = signer.sign(self.hsh)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        raise AttributeError("Cannot be modified")

    @property
    def public_key(self):
        return self._public_key

    @public_key.setter
    def public_key (self, value):
        raise AttributeError("Cannot be modified")


class TransactionPayment:
    """
    Represent transaction payment
    """
    def __init__(self, coin, recv_public_key):
        self._coin = coin
        self._recv_pub_key = recv_public_key

    @property
    def coin(self):
        return self._coin

    @property
    def recv_public_key(self):
        return self._recv_pub_key
