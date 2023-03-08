import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
import hashlib
import time
import random
import secrets
from _math import modPrimePow, is_prime
from tqdm import tqdm


def createParameter():
    start_time = time.time()
    #  hàm kiếm tra số nguyên tố Miller-Rabin primality test.

    def generate_prime():
        Q = random.getrandbits(160)
        while not is_prime(Q):
            Q = random.getrandbits(160)
        return Q


# tạo Q
    Q = generate_prime()

# TẠO R
    R = random.getrandbits(20)

    while True:
    # calculate P
        P = Q * R + 1

    # kiếm tra tính nguyên tố
        if is_prime(P):
            print("P =", P)
            break
        else:
        # tạo lai Q r
            Q = generate_prime()
            R = random.getrandbits(20)

    print("Q =", Q)
    print("R =", R)
    with open(".\\parameters\\P.txt", "w") as f:  # mở p.txt và ghi chuỗi p vào tệp
        f.write(str(P))

    with open(".\\parameters\\P.txt", "r") as file:
        p = int(file.read().strip())  # lấy giá trị P để tính g

# Define the values of Q
    Q = generate_prime()

# Define the file path to write the matching pairs
    file_path = r".\parameters\PR.txt"

# Open the file in write mode
    with open(file_path, "w") as f:
        with tqdm(total=100000, desc="parameters") as pbar:
    # Iterate over values of R from 1 to 100
            for R in range(1, 100000):
        # Calculate the value of P
                P = Q * R + 1
        # Check if P is prime
                if is_prime(P):
            # Write the matching pair (P, R) to the file
                    f.write(f"({P}, {R})\n")
                pbar.update(1)
    print('tao pr thành công')

    input_file_path = r".\parameters\PR.txt"
    output_file_path = r".\parameters\tapG.txt"

# Read the pairs (P, R) from the input file
    with open(input_file_path, "r") as f:
        pairs = [eval(line.strip()) for line in f]

    valid_g = False
    while not valid_g:
    # Select a random pair (P, R)
        P, R = random.choice(pairs)

    # Choose a random value h from [1, P)
        h = random.randint(1, P-1)

    # Compute g = h^R mod P
        g = pow(h, R, P)

    # Check that g^R != 1 mod P
        if pow(g, R, P) != 1:
            valid_g = True

# Write the computed value of g to the output file
    with open(output_file_path, "w") as f:
        f.write(f"{g}\n")

    x = g
    with open(r".\parameters\giatrix.txt", "w") as f:
        f.write(f"{x}\n")
    print('x =', x)
    print("x saved successfully")

# chọn ngẫu nhiên a sau đó in ra màn hình và lưu vào file a.txt
    a = random.randint(2, 200)
    print("a =", a)
    with open(r".\parameters\a.txt", "w") as f:
        f.write(str(a))

    input_file_path = r".\parameters\PR.txt"
    output_file_pathxa = r".\parameters\xa.txt"

# Read the pairs (P, R) from the input file
    with open(input_file_path, "r") as f:
        pairs = [eval(line.strip()) for line in f]

    valid_xa = False
    while not valid_xa:
    # Select a random pair (P, R)
        P, R = random.choice(pairs)

    # Choose a random value h from [1, P)
        h = random.randint(1, P-1)

    # Compute g = h^R mod P
        xa = pow(h, R, P)

    # Check that g^R != 1 mod P
        if pow(xa, R, P) != 1 and xa < g:
            valid_xa = True

# Write the computed value of g to the output file
    with open(output_file_pathxa, "w") as f:
        f.write(f"{xa}\n")

    with open(r".\parameters\xa.txt", "w") as f:
        f.write(str(xa))
# tính khóa công khai của người gửi sau đó ghi vào ya.txt
    y_a = pow(a, xa, p)
    with open(r".\parameters\ya.txt", "w") as f:
        f.write(str(y_a))
    print("Cặp khóa người gửi là (xa = {}; y_a = {})".format(xa, y_a))


    input_file_path = r".\parameters\PR.txt"
    output_file_pathxb = r".\parameters\xb.txt"

# Read the pairs (P, R) from the input file
    with open(input_file_path, "r") as f:
        pairs = [eval(line.strip()) for line in f]

    valid_xb = False
    while not valid_xb:
    # Select a random pair (P, R)
        P, R = random.choice(pairs)

    # Choose a random value h from [1, P)
        h = random.randint(1, P-1)

    # Compute g = h^R mod P
        xb = pow(h, R, P)

    # Check that g^R != 1 mod P
        if pow(xb, R, P) != 1 and xb != g and xb != x:
            valid_xb = True

# Write the computed value of g to the output file
    with open(output_file_pathxb, "w") as f:
        f.write(f"{xb}\n")

    with open(r".\parameters\xb.txt", "w") as f:
        f.write(str(xb))
# tính khóa công khai của người gửi sau đó ghi vào ya.txt
    y_b = pow(a, xb, p)
    with open(r".\parameters\yb.txt", "w") as f:
        f.write(str(y_b))
    print("Cặp khóa người gửi là (xb = {}; y_b = {})".format(xb, y_b))

# tạo ra một chuỗi ngẫu nhiên gồm 16 byte ( 128 bit) sử dụng làm vectơ khởi tạo (IV) trong AES-CBC
    iv = secrets.token_bytes(16)
    with open(r".\parameters\IV.txt", "wb") as f:
        f.write(iv)

    print('Tạo tham số thành công')
    print("Time elapsed: {:.2f} seconds".format(time.time() - start_time))
    return "Created Parameters!"

def signC(path_in, path_out):
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

    x_file = r"./parameters/giatrix.txt"
    yb_file = r"./parameters/yb.txt"
    p_file = r"./parameters/P.txt"

    with open(x_file, "r") as f:
        x = int(f.read().strip())

    with open(yb_file, "r") as f:
        yb = int(f.read().strip())
    
    with open(p_file, "r") as f:
        p = int(f.read().strip())

    k1, k2 = calculate_hash(x, yb, p)

    with open(r"./parameters\k1.txt", "w") as f:
        f.write(k1)

    with open(r"./parameters\k2.txt", "w") as f:
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

    with open(".\\parameters\\k1.txt", "rb") as f:
        key = f.read()
 
    with open(r"./parameters/IV.txt", "rb") as f:
        iv = f.read()

    plaintext_file = path_in

    with open(plaintext_file, "r", encoding='UTF-8') as f:
        plaintext = f.read()

    ciphertext = encrypt_text(plaintext, key, iv)

    encrypted_file = path_out
    with open(encrypted_file, "wb") as f:
        f.write(ciphertext)

    print("Mã hóa thành công.")

    def hash_function(key, plaintext):
        sha256 = hashlib.sha256()
        sha256.update(key + plaintext.encode('utf-8'))
        return sha256.hexdigest()

    with open(".\\parameters\\k2.txt", "r", encoding="utf-8") as file:
        value = file.read().strip()
        k2 = bytes.fromhex(value)

    with open(path_in, "r", encoding="utf-8") as file:
        plaintext = file.read().strip()

    r = hash_function(k2, plaintext)

    with open(path_out, "w", encoding="utf-8") as file:
        file.write(r)

    print('Tính chữ ký r thành công')

    P = r"./parameters\P.txt"
    with open(P, "r") as f:
        P = int(f.read().strip())  
        x_file = r"./parameters\giatrix.txt"
    with open(x_file, "r") as f:
        x = int(f.read().strip())
        x_a = r"./parameters\xa.txt"
    with open(x_a, "r") as f:
        x_a = int(f.read().strip())
        s = (x - x_a + P ) % P
    with open(path_out, "w") as file:
         file.write(str(s))

    print('Tính s thành công')
    print('Signcryption thành công')

    print("Time elapsed: {:.2f} seconds".format(time.time() - start_time))  

    return "signed"
            
def un_signC(path_in, path_out):
    parameters_path = '.\parameters'
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
    with open(rf"{parameters_path}\a.txt", 'r') as f:
        a = int(f.read().strip())
    with open(rf"{parameters_path}\ya.txt", 'r') as f:
        ya = int(f.read().strip())
    with open(rf"{parameters_path}\p.txt", 'r') as f:
        p = int(f.read().strip())
    with open(rf"{parameters_path}\xb.txt", 'r') as f:
        xb = int(f.read().strip())
    with open(rf'{path_in}\s.txt', 'r') as f:
        s = int(f.read().strip())

    def fast_exponentiation(a, s, xb, p):
    # Calculate t = a^s mod p
        t = pow(a, s, p)

    # Calculate k = t^xb mod p
        k = pow(t, xb, p)

        return k
    
    c = modPrimePow(ya, xb, p)
    k = fast_exponentiation(a, s, xb, p)
# Calculate encryption keys
    k11, k21 = calculate_hash(k, c, p)
    with open(rf"{parameters_path}\k11.txt", "w") as f:
        f.write(k11)

    with open(rf"{parameters_path}\k21.txt", "w") as f:
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
        
    with open(f"{parameters_path}\k11.txt", "rb") as f:
        key = f.read()
    
    with open(rf"{parameters_path}\IV.txt", "rb") as f:
        iv = f.read()
   
    with open(f"{path_in}\c.txt", "r") as f:
        ciphertext = f.read()
        ciphertext = base64.b64decode(ciphertext)

    decrypt_text_and_write_to_file(ciphertext, key, iv, f"{path_out}\giaima.txt")

    print("Decryption succeeds")

    def hash_function(key, plaintext):
        sha256 = hashlib.sha256()
        sha256.update(key + plaintext.encode('utf-8'))
        return sha256.hexdigest()

    with open(f"{parameters_path}\k21.txt", "r", encoding="utf-8") as file:
        value = file.read().strip()
        k21 = bytes.fromhex(value)

    with open(f"{path_out}\giaima.txt", "r", encoding="utf-8") as file:
        plaintext = file.read().strip()

    r1 = hash_function(k21, plaintext)

    with open(f"{path_in}/r1.txt", "w", encoding="utf-8") as file:
        file.write(r1)

    print('Tính chữ ký r1 thành công')

    with open(f"{path_in}/r.txt", 'r') as file:
        r = file.readline().strip()

    with open(f"{path_in}/r1.txt", 'r') as file:
        r1 = file.readline().strip()

    if r1 == r:
        print("Valid signature. Unsigncryption successful.")
    else:
        print("Invalid signature. Unsigncryption fails.")
    
    print("Time elapsed: {:.2f} seconds".format(time.time() - start_time))  


# if __name__ == "__main__":
#     signC("#")
#     un_signC("#")
    
