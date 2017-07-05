from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5

import pickle


def create_signature(*args, what_signer):
    """
    Create signature from hashing args and signing what_signer
    :param args: tuple
    :param what_signer: str
    :return: tuple
    """
    hsh = SHA.new(pickle.dumps(args))
    signer = PKCS1_v1_5.new(RSA.importKey(what_signer))
    signature = signer.sign(hsh)

    return hsh, signature