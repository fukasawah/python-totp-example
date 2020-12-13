import base64
import random

LEN=20
data = bytes([random.getrandbits(8) for _ in range(LEN)])
data_base32_str = base64.b32encode(data).decode().replace("=", "")
print(data_base32_str)