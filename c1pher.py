import secrets
from _math import is_prime, modPrimePow, fast_exponentiation
import random
import time
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
import hashlib
import base64
import ast
from colorama import Fore, Back, Style

def generatePrime(bit):
    Q = random.getrandbits(bit)
    while not is_prime(Q):
        Q = random.getrandbits(bit)
    return Q

class Param:
    def __init__(self) -> None:

        pass
    class Cparam:
        def __init__(self, bit) -> None:   
            self.Qbit = bit
            self.Q = generatePrime(self.Qbit)
            self.R = random.getrandbits(20)
            self.P = self.calculateP(bit)
            self.percent = 0
            with open(f"./thamso/P.txt", "w"):
                pass
            
        def calculateP(self, bit):
            while True:
                P = self.Q * self.R + 1
                if is_prime(P):
                    print("P = ", P)
                    return P
                else:
                    self.Q = generatePrime(bit)
                    self.R = random.getrandbits(20)
        
                
        def run(self, bit):
            print("Q = ", self.Q)
            print("R = ", self.R)
            with open(f"./thamso/P.txt", "w") as f:
                f.write(str(self.P))
            Q = generatePrime(self.Qbit)
            with open(f"./thamso/P.txt", "r") as f:
                p = int(f.read().strip())
            with open(f"./thamso/P_R.txt", "w") as f:
                for R in range(1, 100000):
                    P = Q * R + 1
                    if is_prime(P):
                        f.write(f"({P}, {R})\n")
            print("PR keys created!")
            with open(f"./thamso/P_R.txt", "r") as f:
                pairs = [ast.literal_eval(line.strip()) for line in f]
                
            valid_g = False
            while not valid_g:
                P, R = random.choice(pairs)
                h = random.randint(1, P-1)
                g = pow(h, R, P)
                if pow(g, R, P) != 1:
                    valid_g = True
            with open(f"./thamso/tapG.txt", "w") as f:
                f.write(f"{g}\n")
            x= g
            with open(f"./thamso/giatriX.txt", "w") as f:
                f.write(f"{x}\n")
            print("x = ", x)
            print("x saved successfully!")
            a = random.randint(2, 200)
            print("a = ", a)
            with open(f"./thamso/a.txt", "w") as f:
                f.write(str(a))
            with open(f"./thamso/P_R.txt", "r") as f:
                pairs = [ast.literal_eval(line.strip()) for line in f]
            valid_xa = False
            while not valid_xa:
                P, R = random.choice(pairs)
                h = random.randint(1, P-1)
                x_a = pow(h, R, P) 
                if pow(x_a , R, P) != 1 and x_a < g:
                    valid_xa = True
                
            with open(f"./thamso/x_a.txt", "w") as f:
                f.write(f"{x_a}\n")
            with open(f"./thamso/x_a.txt", "w") as f:
                f.write(str(x_a))
            y_a = pow(a, x_a, p)
            with open(f"./thamso/y_a.txt", "w") as f:
                f.write(str(y_a))
            print("sender keys is (x_a = {}; y_a = {})".format(x_a, y_a))
            with open(f"./thamso/P_R.txt", "r") as f:
                pairs = [ast.literal_eval(line.strip()) for line in f]
                
            valid_xb = False
            while not valid_xb :
                P, R = random.choice(pairs)
                h = random.randint(1, P-1)
                xb = pow(h, R, P)
                if pow(xb, R, P) != 1 and xb != g and xb != x:
                    valid_xb = True
            with open(f"./thamso/x_b.txt", "w") as f:
                f.write(f"{xb}\n")
            with open(f"./thamso/x_b.txt", "w") as f:
                f.write(str(xb))
            y_b = pow(a, xb, p)
            with open(f"./thamso/y_b.txt", "w") as f:
                f.write(str(y_a))
            print("sender keys is (x_b = {}; y_b = {})".format(xb, y_b))
            
            iv = secrets.token_bytes(16)
            with open(f"./thamso/IV.txt", "w") as f:
                f.write(str(iv))
            print("Create Parameters succesfully!")
    class Sparam():
        def __init__(self) -> None:
            pass    
        
        def hash_to_128(self, value):
            sha256 = hashlib.sha256(value.encode())
            hex_dig = sha256.hexdigest()
            k1 = hex_dig[:32]
            k2 = hex_dig[32:]
            return k1, k2

        def calculate_hash(self, x, yb, p):
            value = modPrimePow(yb, x, p)
            k1, k2 = self.hash_to_128(str(value))
            return k1, k2

        def encrypt_text(self, plaintext, key, iv):
            backend = default_backend()
            padder = PKCS7(algorithms.AES.block_size).padder()
            padded_data = padder.update(plaintext.encode()) + padder.finalize()
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(padded_data) + encryptor.finalize()
            return base64.b64encode(ciphertext)
        def hash_function(key, plaintext):
            sha256 = hashlib.sha256()
            sha256.update(key + plaintext.encode('utf-8'))
            return sha256.hexdigest()

        
        def run(self, in_path):
            with open(f"./thamso/giatriX.txt", "r") as f:
                x = int(f.read().strip())

            with open(f"./thamso/y_b.txt", "r") as f:
                yb = int(f.read().strip())
    
            with open(f"./thamso/P.txt", "r") as f:
                p = int(f.read().strip())

            k1, k2 = self.calculate_hash(x, yb, p)

            with open(f"./thamso/k1.txt", "w") as f:
                f.write(k1)

            with open(f"./thamso/k2.txt", "w") as f:
                f.write(k2)

            print("Tạo khóa k1 k2 thành công")
            with open(f"./thamso/k1.txt", "rb") as f:
                key = f.read()
 
            with open(f"./thamso/IV.txt", "rb") as f:
                iv = f.read()

            plaintext_file = in_path

            with open(plaintext_file, "r", encoding='UTF-8') as f:
                plaintext = f.read()

            ciphertext = self.encrypt_text(plaintext, key, iv)

            encrypted_file = f"./c.r.s/c.txt"
            with open(encrypted_file, "wb") as f:
                f.write(ciphertext)

            print("Mã hóa thành công.")

            with open(f"./thamso/k2.txt", "r", encoding="utf-8") as file:
                value = file.read().strip()
                k2 = bytes.fromhex(value)

            with open(plaintext_file, "r", encoding="utf-8") as file:
                plaintext = file.read().strip()

            r = self.hash_function(k2, plaintext)

            with open(f"./c.r.s/r.txt", "w", encoding="utf-8") as file:
                file.write(r)

            print('Tính chữ ký r thành công')

            with open(f"./thamso/P.txt", "r") as f:
                P = int(f.read().strip())  
            with open(f"./thamso/giatriX.txt", "r") as f:
                x = int(f.read().strip())
            with open(f"./thamso/x_a.txt", "r") as f:
                x_a = int(f.read().strip())
                s = (x - x_a + P ) % P
            with open(f"./c.r.s//s.txt", "w") as file:
                file.write(str(s))

            print('Tính s thành công')
            print('Signcryption thành công')
            
    class Uparam:
        def __init__(self) -> None:
            pass
        def hash_to_128(self, value):
            sha256 = hashlib.sha256(value.encode())
            hex_dig = sha256.hexdigest()
            k11 = hex_dig[:32]
            k21 = hex_dig[32:]
            return k11, k21
        
        def calculate_hash(self, k, c, p):
            value = (k * c) % p
            k11, k21 = self.hash_to_128(str(value))
            return k11, k21
        
        def decrypt_text_and_write_to_file(self, ciphertext, key, iv, output_file):
            backend = default_backend()
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
            decryptor = cipher.decryptor()
            padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
            unpadder = PKCS7(algorithms.AES.block_size).unpadder()
            plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
            with open(output_file, "wb") as f:
                f.write(plaintext)
        
        def run(self, in_path):
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
            c = modPrimePow(ya, xb, p)
            k = fast_exponentiation(a, s, xb, p)
            # Calculate encryption keys
            k11, k21 = self.calculate_hash(k, c, p)
            with open(f"./thamso/k11.txt", "w") as f:
                f.write(k11)

            with open(f"./thamso/k21.txt", "w") as f:
                f.write(k21)
            print('Tạo khóa k11 k21 thành công')

            
            pass


                        
                
            
            
                    