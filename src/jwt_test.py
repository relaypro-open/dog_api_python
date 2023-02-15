#!/bin/env python3
import jwt

from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

payload_data = {
        "iss": "0d674da4ac7611eda8f78f77fa521b6e"
}

# key_file = open('server.key', 'rb+')
# private_bytes = key_file.read()
# private_key = serialization.load_pem_private_key(
#     private_bytes, None, backend=default_backend()
# )
# cert_file = open('server.crt', 'rb+')
# cert_str = cert_file.read()
# cert_obj = load_pem_x509_certificate(cert_str)
# public_key = cert_obj.public_key()
# token = jwt.encode(payload_data, private_key, algorithm="RS256")
# print(jwt.decode(token, public_key, algorithms=['RS256', ]))

my_secret = 'guest'

token = jwt.encode(
    payload=payload_data,
    key=my_secret,
    algorithm="HS256"
)
print(token)

# print(jwt.decode(token, key=my_secret, algorithms=['HS256', ]))
