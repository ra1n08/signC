import base64
import os
from _math import modPrimePow
from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
import hashlib
import time

start_time = time.time()
def hash_to_128(value):
    sha256 = hashlib.sha256(value.encode())
    hex_dig = sha256.hexdigest()
    k1 = hex_dig[:32]
    k2 = hex_dig[32:]
    return k1, k2

def calculate_hash(x, yb, p):
    value = modPrimePow(yb, x, p)
    k1, k2 = hash_to_128(str(value))
    return k1, k2

x_file = r".\thamso\giatrix.txt"
yb_file = r".\thamso\yb.txt"
p_file = r".\thamso\P.txt"

with open(x_file, "r") as f:
    x = int(f.read().strip())

with open(yb_file, "r") as f:
    yb = int(f.read().strip())
    
with open(p_file, "r") as f:
    p = int(f.read().strip())

k1, k2 = calculate_hash(x, yb, p)

with open(r".\thamso\k1.txt", "w") as f:
    f.write(k1)

with open(r".\thamso\k2.txt", "w") as f:
    f.write(k2)

print ('Tạo khóa k1 k2 thành công')

def encrypt_text(plaintext, key, iv):
    backend = default_backend()
    padder = PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return base64.b64encode(ciphertext)

with open(".\\thamso\\k1.txt", "rb") as f:
    key = f.read()
 
with open(r".\thamso\IV.txt", "rb") as f:
    iv = f.read()

plaintext_file = ".\\filecanmahoa\\filecanmahoa.txt"

with open(plaintext_file, "r", encoding='UTF-8') as f:
    plaintext = f.read()

ciphertext = encrypt_text(plaintext, key, iv)

encrypted_file = ".\\c.r.s\\c.txt"
with open(encrypted_file, "wb") as f:
    f.write(ciphertext)

print("Mã hóa thành công.")

def hash_function(key, plaintext):
    sha256 = hashlib.sha256()
    sha256.update(key + plaintext.encode('utf-8'))
    return sha256.hexdigest()

with open(".\\thamso\\k2.txt", "r", encoding="utf-8") as file:
    value = file.read().strip()
    k2 = bytes.fromhex(value)

with open(".\\filecanmahoa\\filecanmahoa.txt", "r", encoding="utf-8") as file:
    plaintext = file.read().strip()

r = hash_function(k2, plaintext)

with open(".\\c.r.s\\r.txt", "w", encoding="utf-8") as file:
    file.write(r)

print('Tính chữ ký r thành công')

P = r".\thamso\P.txt"
with open(P, "r") as f:
     P = int(f.read().strip())  
     x_file = r".\thamso\giatrix.txt"
with open(x_file, "r") as f:
     x = int(f.read().strip())
     x_a = r".\thamso\xa.txt"
with open(x_a, "r") as f:
     x_a = int(f.read().strip())
     s = (x - x_a + P ) % P
with open(".\\c.r.s\\s.txt", "w") as file:
         file.write(str(s))

print('Tính s thành công')
print('Signcryption thành công')

print("Time elapsed: {:.2f} seconds".format(time.time() - start_time))  




