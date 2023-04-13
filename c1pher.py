import secrets
from _math import is_prime, modPrimePow
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
                    
                
            
            
                    