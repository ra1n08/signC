import secrets
from _math import is_prime, modPrimePow
import ast
from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
import hashlib
import base64
import random

class ParamGenerater:
    @staticmethod
    def generate_prime(bit):
        Q = random.getrandbits(bit)
        while not is_prime(Q):
            Q = random.getrandbits(bit)
        return Q
    
    def run(self, bit):
        # generate Q
        Q = ParamGenerater.generate_prime(bit)
        # generate R
        R = random.getrandbits(20)
        
        while True:
            # calculate P
            P = Q * R + 1
            if is_prime(P):
                print("P=", P)
                with open(f"./thamso/P.txt", "w") as f:
                    f.write(str(P))
                break
            else:
                Q = ParamGenerater.generate_prime(bit)
                R = random.getrandbits(20)
        
        print("Q=", Q)
        print("R=", R)
        
        with open(f"./thamso/P.txt", "r") as f:
            p = int(f.read().strip())
            
        # generate Q value
        Q = ParamGenerater.generate_prime(bit)
        
        PR_path = f"./thamso/P_R.txt"
        with open(PR_path, "w") as f:
            # iterate over values of R from 1 to 100
            for R in range(1, 100000):
                # calculate the value of P
                P = Q * R + 1
                # check if P is prime
                if is_prime(P):
                    f.write(f"({P}, {R})\n")
        print("generated P and R")
        
        with open(PR_path, "r") as f:
            pairs = [ast.literal_eval(line.strip()) for line in f]
        
        valid_g = False
        while not valid_g:
            # select random pairs
            P, R = random.choice(pairs)
            # choose a random value h fro, [(1, P)]
            h = random.randint(1, P-1)
            
            # compute g = h^R !=1 mod P
            g = pow(h, R, P)
            # check that g^R != 1 mod P
            if pow(g, R, P) != 1:
                valid_g = True
        
        with open(f"./thamso/tapG.txt", "w") as f:
            f.write(f"{g}\n")
        
        x = g
        with open(f"./thamso/giatriX.txt", "w") as f:
            f.write(f"{x}\n")
        print("X=", x)
        print("X saved successfully!")
        
        # choose random A then print out and save to a.txt
        a = random.randint(2, 200)
        print("a=", a)
        with open(f"./thamso/a.txt", "w") as f:
            f.write(str(a))
        
        # with open(PR_path, "r") as f:
        #     pairs = [ast.literal_eval(l.strip()) for l in f]
            
        valid_xa = False
        while not valid_xa:
            # select random pairs (P, R)
            P, R = random.choice(pairs)
            # choose a random value h from [(1, P)]
            h = random.randint(1, P-1)
            # compute g = h^R mod P
            xa = pow(h, R, P)
            # check that g^R !=1 < g
            if pow(xa, R, P) != 1 and xa < g:
                valid_xa = True
        
        with open(f"./thamso/Xa.txt", "w") as f:
            f.write(f"{xa}\n")
        with open(f"./thamso/Xa.txt", "w") as f:
            f.write(str(xa))
        # print(f"x_a key {xa} saved successfully")
        # calculate public key of sender then write to ya.txt
        y_a = pow(a, xa, p)
        with open(f"./thamso/Ya.txt", "w") as f:
            f.write(str(y_a))
        print(f"x_a key {xa} and y_a key {y_a} saved successfully")
        
        # with open(PR_path, "r") as f:
        #     pairs = [ast.literal_eval(l.strip()) for l in f]
        
        valid_xb = False
        while not valid_xb:
            # select a random pair (P, R)
            P, R = random.choice(pairs)
            # choose a random value h from [(1, P)]
            h = random.randint(1, P-1)
            # Compute g = h^R mod P
            xb = pow(h, R, P)
            # Check that g^R != 1 mod P
            if pow(xb, R, P) != 1 and xb !=g and xb != x:
                valid_xb = True
        
        with open(f"./thamso/Xb.txt", "w") as f:
            f.write(f"{xb}\n")
        with open(f"./thamso/Xh.txt", "w") as f:
            f.write(str(xb))
        
        y_b = pow(a, xb ,p)
        with open(f"./thamso/Yb.txt", "w") as f:
            f.write(str(y_b))
        print(f"x_b key {xb} and y_b key {y_b} saved successfully")
        
        iv = secrets.token_bytes(16)
        with open(f"./thamso/iv.txt", "wb") as f:
            f.write(iv)
        print("generated parameters!")

class Sign:
    @staticmethod
    def hash_to_128(value):
        sha256 = hashlib.sha256(value.encode())
        hex_dig = sha256.hexdigest()
        k1 = hex_dig[:32]
        k2 = hex_dig[32:]
        return k1, k2
    
    @staticmethod calculate_hash(x, yb, p):
    value = modPrimePow(yb, x, p)
    k1, k2 = hash_to_128(str(value))
    return k1, k2

    def run(self, inpF):
        pass
        