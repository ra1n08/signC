import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
import hashlib
import time

start_time = time.time()
def hash_to_128(value):
    sha256 = hashlib.sha256(value.encode())
    hex_dig = sha256.hexdigest()
    k11 = hex_dig[:32]
    k21 = hex_dig[32:]
    return k11, k21

def calculate_hash(k, c, p):
    value = (k * c) % p
    k11, k21 = hash_to_128(str(value))
    return k11, k21

# Read values from files
with open(f'./thamso/a.txt', 'r') as f:
    a = int(f.read().strip())
with open(f'./thamso/y_a.txt', 'r') as f:
    ya = int(f.read().strip())
with open(f'./thamso/P.txt', 'r') as f:
    p = int(f.read().strip())
with open(f'./thamso/x_b.txt', 'r') as f:
    xb = int(f.read().strip())
with open(f'./c.r.s/s.txt', 'r') as f:
    s = int(f.read().strip())

def fast_exponentiation(a, s, xb, p):
    # Calculate t = a^s mod p
    t = pow(a, s, p)

    # Calculate k = t^xb mod p
    k = pow(t, xb, p)

    return k

def modPrimePow(a, b, p):
    ret = 1
    a %= p
    b %= p - 1
    while b > 0:
        if b % 2 > 0:
            ret = (ret * a) % p
        a = (a * a) % p
        b //= 2
    return ret
    
c = modPrimePow(ya, xb, p)
k = fast_exponentiation(a, s, xb, p)
# Calculate encryption keys
k11, k21 = calculate_hash(k, c, p)
with open(r"./thamso/k11.txt", "w") as f:
    f.write(k11)

with open(r"./thamso/k21.txt", "w") as f:
    f.write(k21)
print ('Tạo khóa k11 k21 thành công')

def decrypt_text_and_write_to_file(ciphertext, key, iv, output_file):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    with open(output_file, "wb") as f:
        f.write(plaintext)
        
with open(".\\thamso\\k11.txt", "rb") as f:
    key = f.read()
    
with open(r"./thamso/IV.txt", "rb") as f:
    iv = f.read()
   
with open(".\\c.r.s\\c.txt", "r") as f:
    ciphertext = f.read()
    ciphertext = base64.b64decode(ciphertext)

decrypt_text_and_write_to_file(ciphertext, key, iv, ".\\outSign.txt")

print("Decryption succeeds")

def hash_function(key, plaintext):
    sha256 = hashlib.sha256()
    sha256.update(key + plaintext.encode('utf-8'))
    return sha256.hexdigest()

with open(".\\thamso\\k21.txt", "r", encoding="utf-8") as file:
    value = file.read().strip()
    k21 = bytes.fromhex(value)

with open(".\\outSign.txt", "r", encoding="utf-8") as file:
    plaintext = file.read().strip()

r1 = hash_function(k21, plaintext)

with open(".\\c.r.s\\r1.txt", "w", encoding="utf-8") as file:
    file.write(r1)

print('Tính chữ ký r1 thành công')

with open('.\\c.r.s\\r.txt', 'r') as file:
    r = file.readline().strip()

with open('.\\c.r.s\\r1.txt', 'r') as file:
    r1 = file.readline().strip()

if r1 == r:
    print("Valid signature. Unsigncryption successful.")
else:
    print("Invalid signature. Unsigncryption fails.")
    
print("Time elapsed: {:.2f} seconds".format(time.time() - start_time))  
