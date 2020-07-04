import base64

b1 = base64.b64decode('xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p')
b2 = base64.b64decode('h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU')

def byte_xor(ba1, ba2):
    return bytes([a ^ b for a, b in zip(ba1, ba2)])

flag = byte_xor(b1, b2)

print(flag)